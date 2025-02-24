import datetime
def nowprint(msg):
    print(f"{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} :: {msg} done")
nowprint("start script")
from multiprocessing import Process
nowprint("multiprocessing import")
from pyforestscan.handlers import read_lidar, create_geotiff
nowprint("pyforestscan.handlers import")
from pyforestscan.calculate import assign_voxels, calculate_pad, calculate_pai
nowprint("pyforestscan.calculate import")
from pyforestscan.visualize import plot_metric
nowprint("pyforestscan.visualize import")
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
slicer = slice(1, 2) # slice(1, 2) # slice to process, e.g. slice(1, 2) is equivalent to [1:2] aka second item from the list
nowprint("settings pyforestscan")
for laz in lazzes[slicer]:
    nowprint(f"laz: {inputdir}{laz}")
    arrays = read_lidar(f"{inputdir}{laz}", epsgin, hag=True)
    nowprint("read_lidar")
    voxel_resolution = (5, 5, 1)
    voxels, extent = assign_voxels(arrays[0], voxel_resolution)
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
