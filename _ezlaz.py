import datetime
def nowprint(msg):
    print(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :: {msg} done")
nowprint("start script")
import os
nowprint("os import")
import json
nowprint("json import")
import pdal
nowprint("pdal import")
import numpy as np
nowprint("numpy import")
import tempfile
nowprint("tempfile import")
from multiprocessing import Pool, cpu_count
nowprint("multiprocessing import")
from pyforestscan.pipeline import _crop_polygon, _filter_radius, _hag_delaunay, _hag_raster
nowprint("pyforestscan.pipeline")
# from multiprocessing import Process
# nowprint("multiprocessing import")
from pyforestscan.handlers import read_lidar, create_geotiff
nowprint("pyforestscan.handlers import")
from pyforestscan.calculate import assign_voxels, calculate_pad, calculate_pai
nowprint("pyforestscan.calculate import")
from pyforestscan.visualize import plot_metric
nowprint("pyforestscan.visualize import")

### BO
def process_chunk(chunk_data, start, end, has_hag, temp_filename):
    """Processes a single PDAL chunk and writes it to the memory-mapped file."""
    
    # Open the memory-mapped file in read/write mode
    mmap = np.memmap(temp_filename, dtype=[("X", np.float32), ("Y", np.float32), 
                                           ("Z", np.float32), ("HeightAboveGround", np.float32)],
                     mode="r+", shape=(end,))  # Adjust shape for partial chunking

    # Write data directly to memory-mapped file
    mmap["X"][start:end] = chunk_data["X"].astype(np.float32)
    mmap["Y"][start:end] = chunk_data["Y"].astype(np.float32)
    mmap["Z"][start:end] = chunk_data["Z"].astype(np.float32)

    if has_hag:
        mmap["HeightAboveGround"][start:end] = chunk_data["HeightAboveGround"].astype(np.float32)
    else:
        mmap["HeightAboveGround"][start:end] = np.nan  # Assign NaN efficiently

    # Explicitly flush changes to disk
    mmap.flush()

def ez_read_lidar(input_file, srs, bounds=None, thin_radius=None, hag=False, hag_dtm=False, dtm=None, 
                  crop_poly=False, poly=None, chunk_size=10**6, return_array=False):
    """
    Reads and processes a LiDAR point cloud file using PDAL **without requiring iterator()**.
    Uses **filters.splitter** to process large `.LAZ` files in chunks.
    """

    if not os.path.isfile(input_file):
        raise FileNotFoundError(f"No such file: '{input_file}'")

    las_extensions = ('.las', '.laz')
    copc_extensions = ('.copc', '.copc.laz')
    ept_file = ('ept.json')

    file_lower = input_file.lower()
    if file_lower.endswith(las_extensions):
        reader = "readers.las"
    elif file_lower.endswith(copc_extensions):
        reader = "readers.copc"
    elif file_lower.endswith(ept_file):
        reader = "readers.ept"
    else:
        raise ValueError("Unsupported file format. Must be .las, .laz, .copc, .copc.laz, or ept.json.")

    if hag and hag_dtm:
        raise ValueError("Cannot use both 'hag' and 'hag_dtm' options at the same time.")

    pipeline_stages = []

    if crop_poly and poly:
        pipeline_stages.append(_crop_polygon(poly))

    if thin_radius:
        if thin_radius <= 0:
            raise ValueError("Thinning radius must be a positive number.")
        pipeline_stages.append(_filter_radius(thin_radius))

    if hag:
        pipeline_stages.append(_hag_delaunay())

    if hag_dtm:
        if not dtm or not os.path.isfile(dtm):
            raise FileNotFoundError(f"Missing DTM file: '{dtm}'")
        pipeline_stages.append(_hag_raster(dtm))

    # **Use filters.splitter to process chunks instead of loading full file**
    splitter = {
        "type": "filters.splitter",
        "length": 1000,  # Adjust tile size based on available memory
        "buffer": 50
    }

    pipeline_stages.append(splitter)

    # **Create a temporary memory-mapped file**
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mmap") as temp_file:
        temp_filename = temp_file.name

    num_workers = min(4, cpu_count())  # Use up to 4 parallel processes
    total_points = 0  # Track total number of points

    # **Manually Execute PDAL in Chunks**
    chunk_ranges = []
    base_pipeline = {
        "type": reader,
        "spatialreference": srs,
        "filename": input_file
    }

    main_pipeline_json = {
        "pipeline": [base_pipeline] + pipeline_stages
    }

    main_pipeline = pdal.Pipeline(json.dumps(main_pipeline_json))
    main_pipeline.execute()

    for chunk in main_pipeline.arrays:
        chunk_size_actual = len(chunk)
        chunk_ranges.append((chunk, total_points, total_points + chunk_size_actual, "HeightAboveGround" in chunk.dtype.names, temp_filename))
        total_points += chunk_size_actual  # Update total point count

    # **Process chunks in parallel**
    with Pool(num_workers) as pool:
        pool.starmap(process_chunk, chunk_ranges)

    # **Read memory-mapped file in read mode**
    mmap = np.memmap(temp_filename, dtype=[("X", np.float32), ("Y", np.float32), 
                                           ("Z", np.float32), ("HeightAboveGround", np.float32)],
                     mode="r", shape=(total_points,))

    if return_array:
        return mmap.copy()  # Load into memory only when needed

    return mmap  # Return mmap for iterator usage
### EO

nowprint("ez_read_lidar")

# Some q&d folder en file settings. Could loop all file in a folder or use external configurtaion file.
inputdir = "data/"
outputdir = "output/"
# Could distinct input (from file) and output (as needed) epsg
epsgin = "EPSG:28992"
epsgout = epsgin
#epsgout = "EPSG:xxxx" # Another epsg
# NOTE: when using "EPSG:28992" as input epsg and "EPSG:3035" as output, the resulting tiff could not be opened
# Test AHN laz data Cannenburgergat, Nijmegen, Imbosch
lazzes = ["2023_C_27CZ2.LAZ", "2024_C_40CZ2.LAZ", "C_33DZ2.LAZ"]
slicer = slice(0,1) # slice(1, 2) # Use slice (zero based) to determine files to process, e.g. slice(1, 2) is equivalent to [1:2] aka second item from the list
nowprint("settings pyforestscan")
for laz in lazzes[slicer]:
    nowprint(f"get laz: {inputdir}{laz}")
    #arrays = read_lidar(f"{inputdir}{laz}", epsgin, hag=True)
    #arrays = ez_read_lidar(f"{inputdir}{laz}", epsgin, hag=True, return_array=True)
    arrays = ez_read_lidar(f"{inputdir}{laz}", epsgin, hag=True)
    nowprint("read_lidar")
    # Ensure HeightAboveGround is present
    if "HeightAboveGround" not in arrays.dtype.names:
        raise ValueError("HeightAboveGround field is missing in the LiDAR data, but is required for assign_voxels.")
    nowprint("check HeightAboveGround")
    voxel_resolution = (5, 5, 1)
    # With original function read_lidar
    #voxels, extent = assign_voxels(arrays[0], voxel_resolution)
    # With adjusted function ez_read_lidar
    voxels, extent = assign_voxels(arrays, voxel_resolution)
    nowprint("assign_voxels")
    pad = calculate_pad(voxels, voxel_resolution[-1])
    nowprint("calculate_pad")
    pai = calculate_pai(pad)
    nowprint("calculate_pai")
    create_geotiff(pai, f"{outputdir}{laz}.tiff", epsgout, extent)
    nowprint(f"create_geotiff: {outputdir}{laz}.tiff")
    plot_metric('Plant Area Index', pai, extent, metric_name='PAI', cmap='viridis', fig_size=None)
    # p = Process(target=plot_metric, args=('Plant Area Index', pai, extent, f'metric_name="PAI"', f'cmap="viridis"', f'fig_size=None'))
    # p.start()
    # p.join()
    nowprint("plot_metric")
