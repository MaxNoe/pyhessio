# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
Simple python wrapper for hessioxxx c library.
"""

import numpy as np
import os
import ctypes

__all__ = ['move_to_next_event','move_to_next_mc_event',
           'file_open','file_close', 'close_file',
           'get_global_event_count','get_run_number',
           'get_num_telescope','get_telescope_with_data_list',
           'get_teldata_list', 'get_telescope_position',
           'get_num_teldata','get_num_channel','get_num_pixels',
           'get_num_samples','get_adc_sample','get_adc_sum',
           'get_pedestal','get_calibration','get_pixel_position',
           'get_pixel_timing_timval','get_pixel_shape','get_pixel_area',
           'get_mirror_area','get_pixel_timing_num_times_types',
           'get_pixel_timing_threshold','get_pixel_timing_peak_global',
           'get_mc_shower_primary_id','get_mc_shower_h_first_int',
           'get_mc_event_xcore', 'get_mc_event_ycore' ,'get_mc_shower_energy',
           'get_mc_event_offset_fov','get_mc_number_photon_electron',
           'get_mc_shower_azimuth' ,'get_mc_shower_altitude','get_adc_known',
           'get_ref_shape' ,'get_ref_step','get_time_slice',
           'get_ref_shapes',  'get_nrefshape' ,'get_lrefshape',
           'get_tel_event_gps_time' ,'get_tel_event_gps_time',
           'get_central_event_teltrg_list','get_num_tel_trig',
           'get_central_event_gps_time','get_camera_rotation_angle',
           'get_mirror_number', 'get_optical_foclen', 'get_telescope_ids',
           'HessioChannelIndexError', 'HessioTelescopeIndexError','HessioGeneralError']




_path = os.path.dirname(__file__)
lib = np.ctypeslib.load_library('pyhessioc', _path)

lib.close_file.restype = None
lib.file_open.argtypes = [ctypes.c_char_p]
lib.file_open.restype = ctypes.c_int
lib.get_adc_sample.argtypes = [ctypes.c_int,ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_uint16, flags="C_CONTIGUOUS")]
lib.get_adc_sample.restype = ctypes.c_int
lib.get_adc_sum.argtypes = [ctypes.c_int,ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_int32, flags="C_CONTIGUOUS")]
lib.get_adc_sum.restype = ctypes.c_int
lib.get_calibration.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_calibration.restype=ctypes.c_int
lib.get_pedestal.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_pedestal.restype=ctypes.c_int
lib.get_global_event_count.restype = ctypes.c_int
lib.get_mirror_area.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_mirror_area.restype = ctypes.c_int
lib.get_num_channel.argtypes = [ctypes.c_int]
lib.get_num_channel.restype = ctypes.c_int
lib.get_num_pixels.argtypes = [ctypes.c_int]
lib.get_num_pixels.restype = ctypes.c_int
lib.get_num_samples.argtypes = [ctypes.c_int]
lib.get_num_samples.restype = ctypes.c_int
lib.get_num_teldata.restype = ctypes.c_int
lib.get_num_telescope.restype = ctypes.c_int
lib.get_num_tel_trig.restype = ctypes.c_int
lib.get_pixel_timing_num_times_types.argtypes = [ctypes.c_int]
lib.get_pixel_timing_num_times_types.restype = ctypes.c_int
lib.get_pixel_position.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS"),
                                  np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_pixel_position.restype=ctypes.c_int
lib.get_pixel_timing_peak_global.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_float, flags="C_CONTIGUOUS")]
lib.get_pixel_timing_peak_global.restype = ctypes.c_int
lib.get_pixel_timing_threshold.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_int, flags="C_CONTIGUOUS")]
lib.get_pixel_timing_threshold.restype = ctypes.c_int
lib.get_pixel_timing_timval.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_float, flags="C_CONTIGUOUS")]
lib.get_pixel_timing_timval.restype=ctypes.c_int
lib.get_pixel_shape.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_pixel_shape.restype=ctypes.c_int
lib.get_pixel_area.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_pixel_area.restype=ctypes.c_int
lib.get_run_number.restype = ctypes.c_int
lib.get_telescope_with_data_list.argtypes = [np.ctypeslib.ndpointer(ctypes.c_int, flags="C_CONTIGUOUS")]
lib.get_telescope_with_data_list.restype = ctypes.c_int
lib.get_telescope_position.argtypes=[ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_telescope_position.restype=ctypes.c_int
lib.move_to_next_event.argtypes = [np.ctypeslib.ndpointer(ctypes.c_int)]
lib.move_to_next_event.restype = ctypes.c_int
lib.move_to_next_mc_event.argtypes = [np.ctypeslib.ndpointer(ctypes.c_int)]
lib.move_to_next_mc_event.restype = ctypes.c_int
lib.get_mc_event_xcore.restype = ctypes.c_double
lib.get_mc_event_ycore.restype = ctypes.c_double
lib.get_mc_event_offset_fov.argtypes = [np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_mc_event_offset_fov.restype = ctypes.c_int
lib.get_mc_number_photon_electron.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_int, flags="C_CONTIGUOUS")]
lib.get_mc_number_photon_electron.restype = ctypes.c_int
lib.get_mc_shower_energy.restype = ctypes.c_double
lib.get_mc_shower_azimuth.restype = ctypes.c_double
lib.get_mc_shower_altitude.restype = ctypes.c_double
lib.get_mc_shower_primary_id.restype = ctypes.c_int
lib.get_mc_shower_h_first_int.restype = ctypes.c_double
lib.get_adc_known.restype = ctypes.c_int
lib.get_adc_known.argtypes = [ctypes.c_int,ctypes.c_int,ctypes.c_int]
lib.get_ref_shape.restype = ctypes.c_double
lib.get_ref_shape.argtypes =  [ctypes.c_int,ctypes.c_int,ctypes.c_int]
lib.get_time_slice.restype = ctypes.c_double
lib.get_time_slice.argtypes  =  [ctypes.c_int]
lib.get_ref_step.restype = ctypes.c_double
lib.get_ref_step.argtypes  =  [ctypes.c_int]
lib.get_ref_shapes.restypes = ctypes.c_int
lib.get_ref_shapes.argtypes =[ctypes.c_int,ctypes.c_int, np.ctypeslib.ndpointer(ctypes.c_double, flags="C_CONTIGUOUS")]
lib.get_nrefshape.restypes = ctypes.c_int
lib.get_nrefshape.argtypes = [ctypes.c_int]
lib.get_lrefshape.restypes = ctypes.c_int
lib.get_lrefshape.argtypes = [ctypes.c_int]
lib.get_tel_event_gps_time.restype = ctypes.c_int
lib.get_tel_event_gps_time.argtypes = [ctypes.c_int,np.ctypeslib.ndpointer(ctypes.c_long, flags="C_CONTIGUOUS"), np.ctypeslib.ndpointer(ctypes.c_long, flags="C_CONTIGUOUS")]
lib.get_central_event_gps_time.restype = ctypes.c_int
lib.get_central_event_gps_time.argtypes =  [np.ctypeslib.ndpointer(ctypes.c_long, flags="C_CONTIGUOUS"), np.ctypeslib.ndpointer(ctypes.c_long, flags="C_CONTIGUOUS")]
lib.get_central_event_teltrg_list.restype = ctypes.c_int
lib.get_central_event_teltrg_list.argtypes = [np.ctypeslib.ndpointer(ctypes.c_int, flags="C_CONTIGUOUS")]
lib.get_camera_rotation_angle.argtypes = [ctypes.c_int]
lib.get_camera_rotation_angle.restype = ctypes.c_double
lib.get_mirror_number.restype = ctypes.c_int
lib.get_mirror_number.argtypes = [ctypes.c_int]
lib.get_optical_foclen.argtypes = [ctypes.c_int]
lib.get_optical_foclen.restype = ctypes.c_double
lib.get_telescope_ids.argtypes = [np.ctypeslib.ndpointer(ctypes.c_int, flags="C_CONTIGUOUS")]
lib.get_telescope_ids.restype = ctypes.c_int



TEL_INDEX_NOT_VALID  =-2
PIXEL_INDEX_NOT_VALID =-3


class HessioError(Exception):
    pass


class HessioGeneralError(HessioError):
    pass


class HessioTelescopeIndexError(HessioError):
    pass


class HessioChannelIndexError(HessioError):
    pass


def move_to_next_event(limit=0):
    """
    Read data form input file
    and fill corresponding container
    Data can be then access with
    other available functions in
    this module
    By default all events are computed

    :param limit: limit the number of event generated
    :type limit: int, optional
    :return: run number and event id in case of SUCCESS, otherwise -1,-1
    :rtype: tuple(int,int):
    """
    result = np.zeros(1, dtype=np.int32)
    res = 0
    evt_num = 0
    while res >= 0 and (limit == 0 or evt_num < limit):
        res = lib.move_to_next_event(result)
        if res != -1:
            yield res, result[0]
            evt_num = evt_num + 1


def move_to_next_mc_event(limit=0):
    """
    Read data form input file
    and fill corresponding container
    Data can be then access with
    other available functions in
    this module.
    This iterator scans all the simulated events,
    not only the triggered ones.
    By default all events are computed

    :param limit: limit the number of event generated
    :type limit: int, optional
    :return: run number and event id in case of success, otherwise -1,-1
    :rtype: tuple(int,int):
    """
    result = np.zeros(1, dtype=np.int32)
    res = 0
    sim_evt_num = 0
    while res >= 0 and (limit == 0 or sim_evt_num < limit):
        res = lib.move_to_next_mc_event(result)
        if res != -1:
            yield res, result[0]
            sim_evt_num = sim_evt_num + 1


def file_open(filename):
    """
    Open input data file

    :param filename: file name to be opened
    :type filename: str
    :return: 0 in case of success, otherwise -1
    :rtype: int:
    """
    b_filename = filename.encode('utf-8')
    return lib.file_open(b_filename)


def file_close():
    """
    Close opened iobuf
    """
    lib.close_file()

def close_file():
    """
    Close opened iobuf
    """
    lib.close_file()

def get_global_event_count():
    """
    :return: counter for system trigger
    :rtype: int:
    """
    return lib.get_global_event_count()

def get_run_number():
    """
    :return: run number read in data file or -1 if not available
    :rtype: int
    :raise: HessioGeneralError: when hsdata->run_header.run is not available
    """
    run =  lib.get_run_number()
    if run > 0 : return run
    else:
        raise(HessioGeneralError("run number not available"))


def get_num_telescope():
    """
    :return: the number of telescopes in current run.
    :rtype: int
    :raise: HessioGeneralError: when hsdata->event.num_tel is not available
    """
    number =  lib.get_num_telescope()
    if number > 0 : return number
    else:
        raise(HessioGeneralError("number of telescopes in current run not available"))


def get_num_tel_trig():
    """
    :return:  How many telescopes triggered in Central Event
    :rtype: int
    :raise:  HessioGeneralError: when hsdata is not available
    """
    number =  lib.get_num_tel_trig()
    if number > 0 : return number
    else:
        raise(HessioGeneralError("number of triggered telescopes in central event not available"))



def get_mirror_area(telescope_id):
    """
    :param telescope_id: Telescope's id
    :type telescope_id: int
    :return: total area of individual mirrors corrected for inclination [m^2].
    :rtype: int
    :raise: HessioGeneralError: when hsdata->camera_set[itel].mirror_area not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """

    data = np.zeros(1,dtype=np.double)
    result = lib.get_mirror_area(telescope_id,data)
    if result == 0:
        return data[0]
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    raise(HessioGeneralError("hsdata->camera_set[itel].mirror_area not available"))


def get_telescope_with_data_list():
    """
    :return: list of telescope with data for current event
    :rtype: numpy.ndarray(num_teldata,dtype=np.int32)
    :raise: HessioGeneralError: when information is not available
    """
    try:
        return get_teldata_list()
    except:
        raise(HessioGeneralError("hsdata->event.teldata_list is not available"))


def get_teldata_list():
    """
    :return: list of IDs of telescopes with data for current event
    :rtype: numpy.ndarray(num_teldata,dtype=np.int32)
    :raise: HessioGeneralError: when information is not available
    """
    num_teldata= get_num_teldata()
    if num_teldata >= 0:
        array = np.zeros(num_teldata,dtype=np.int32)
        lib.get_telescope_with_data_list(array)
        return array
    else:
        raise(HessioGeneralError("hsdata->event.num_teldata is not available"))


def get_telescope_position(telescope_id):
    """
    :param telescope_id: The telescope id
    :type telescope_id: int
    :return: Telescope position for a telescope id.

    * x is counted from array reference position towards North
    * y towards West
    * z upwards

    :rtype: numpy.ndarray(3,dtype=np.double)
    :raise: HessioGeneralError: when  telescope position not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    pos = np.zeros(3,dtype=np.double)

    result = lib.get_telescope_position(telescope_id,pos)
    if result == 0:
        return pos
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no telescope position for telescope "
                              + str(telescope_id)))


def get_num_teldata():
    """
    :return: number of telescopes for which we actually have data
    :rtype: int
    :raise: HessioGeneralError when hsdata->event.num_teldata is not available
    """
    number =  lib.get_num_teldata()
    if number >= 0:
        return number
    else:
        raise(HessioGeneralError("hsdata->event.num_teldata is not available"))


def get_num_channel(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: type of channel used

    * HI_GAIN          0     Index to high-gain channels in adc_sum, adc_sample, pedestal, ...
    * LO_GAIN          1     Index to low-gain channels in adc_sum, adc_sample, pedestal, ...

    :rtype: int
    :raise: HessioGeneralError: when hsdata->event.teldata[itel].raw
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    result =  lib.get_num_channel(telescope_id)
    if result >= 0: return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError(" hsdata->event.teldata[itel].raw not available"))


def get_num_pixels(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: the number of pixels in the camera (as in configuration)
    :rtype: int
    :raise: HessioGeneralError: when hsdata->camera_set[itel].num_pixels
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    result = lib.get_num_pixels(telescope_id)
    if result >= 0 : return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->camera_set[itel].num_pixels not available"))


def get_pixel_timing_threshold(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: PixelTiming threshold: Minimum base-to-peak raw amplitude difference applied in pixel selection
    :rtype: numpy.int32
    :raise: HessioGeneralError: When hsdata->event.teldata[itel].pixtm
    :raise: HessioTelescopeIndexError: when  no telescope exist with this id
    """
    threshold = np.zeros(1,dtype=np.int32)
    result = lib.get_pixel_timing_threshold(telescope_id,threshold)
    if result == 0: return threshold[0]
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->event.teldata[itel].pixtm not available"))


def get_pixel_timing_peak_global(telescope_id):

    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: PixelTiming peak_global: Camera-wide (mean) peak position [time slices]
    :rtype: numpy.float32
    :raise: HessioGeneralError: when hsdata->event.teldata[itel].pixtm; not available
    :raise: HessioTelescopeIndexError when no telescope exist with this id
    """
    peak = np.zeros(1,dtype=np.float32)
    result = lib.get_pixel_timing_peak_global(telescope_id,peak)
    if result == 0: return peak[0]
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->event.teldata[itel].pixtm; not available"))


def get_pixel_timing_num_times_types(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: how many different types of times can we store
    :rtype: int
    :raise: HessioGeneralError: when hsdata->event.teldata[itel].pixtm->num_types not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    result = lib.get_pixel_timing_num_times_types(telescope_id)
    if result >= 0: return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->event.teldata[itel].pixtm->num_types  not available"))


def get_num_samples(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: the number of samples (time slices) recorded
    :rtype: int
    :raise: HessioGeneralError: when data->event.teldata[itel].raw->num->samples not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    result = lib.get_num_samples(telescope_id)
    if result >= 0: return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("ata->event.teldata[itel].raw->num->samples not available"))


def get_adc_sample(telescope_id,channel):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :param channel: (0->HI_GAIN, 1->LOW_GAIN)
    :type channel: int
    :return: pulses sampled
    :rtype: numpy.array(npix,ntimeslices,dtype=np.uint16)
    :raise: HessioGeneralError: when information is not available
    :raise: HessioTelescopeIndexError when no telescope exist with this id
    :raise: HessioChannelIndexError when channel does not exist for this telescope
    """
    if channel > get_num_channel(telescope_id)-1:
        raise(HessioChannelIndexError("telescope " + str(telescope_id) + " has not got channel " + str(channel)))

    try:
        npix = get_num_pixels(telescope_id)
        ntimeslices = get_num_samples(telescope_id)


        if ( ntimeslices > 0):
            data = np.zeros(npix*ntimeslices,dtype=np.uint16)
            result = lib.get_adc_sample(telescope_id,channel ,data)
            if result == 0:
                d_data = data.reshape(npix,ntimeslices)
                return d_data
            elif result == TEL_INDEX_NOT_VALID:
                raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
            else:
                raise(HessioGeneralError("adc sample not available for telescope "+
                                       str(telescope_id) +
                                       " and channel " + str(channel)))
        else:
            return np.zeros(0)


    except HessioTelescopeIndexError: raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    except HessioGeneralError: raise (HessioGeneralError("adc sample not available for telescope "+
                                   str(telescope_id) +
                                   " and channel " + str(channel)))


def get_adc_sum(telescope_id,channel):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :param channel: (0->HI_GAIN, 1->LOW_GAIN)
    :type channel: int
    :return: sum of ADC values.
    :rtype: np.zeros(npix,dtype=np.int32)
    :raise: HessioGeneralError: when No adc_sum for telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    :raise: HessioChannelIndexError: when channel does not exist for this telescope
    """

    if channel > get_num_channel(telescope_id)-1:
        raise(HessioChannelIndexError("telescope " + str(telescope_id) + " has not got channel " + str(channel)))

    npix = get_num_pixels(telescope_id)
    data = np.zeros(npix,dtype=np.int32)
    result = lib.get_adc_sum(telescope_id,channel ,data)
    if result == 0:
        return data
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("No adc_sum for telescope "+ str(telescope_id)))


def get_pixel_timing_timval(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: PixelTiming.timval
    :rtype:  numpy.array(npix,ntimes,dtype=np.float32)
    :raise: HessioGeneralError: when hsdata->event.teldata[itel]->timval[ipix][itimes] not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)
    ntimes = get_pixel_timing_num_times_types(telescope_id)
    data = np.zeros(npix*ntimes,dtype=np.float32)
    result = lib.get_pixel_timing_timval(telescope_id,data)
    if result == 0:
        d_data = data.reshape(npix,ntimes)
        return d_data
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no pixel timing timval for telescope "
                              + str(telescope_id)))


def get_calibration(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: calibration numpy array (num_gain dimention)
    :rtype: nupy.array(ngain,npix,dtype=np.double)
    :raise: HessioGeneralError: when data not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)

    ngain =  get_num_channel(telescope_id)
    ngain = 2
    calibration = np.zeros(ngain*npix,dtype=np.double)

    result = lib.get_calibration(telescope_id,calibration)
    if result == 0:
        d_cal = calibration.reshape(ngain,npix)
        return d_cal
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no calibration data for telescope "
                              + str(telescope_id)))


def get_pedestal(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: pedestal
    :rtype: numpy.ndarray(ngain,npix,dtype=np.double)
    :raise: HessioGeneralError: when data not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)

    ngain =  get_num_channel(telescope_id)
    pedestal = np.zeros(ngain*npix,dtype=np.double)

    result = lib.get_pedestal(telescope_id,pedestal)
    if result == 0:
        d_ped = pedestal.reshape(ngain,npix)
        return d_ped
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no pedestal data for telescope "
                              + str(telescope_id)))


def get_pixel_position(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: pixels position for a telescope id (pos_x,pos_y)
    :rtype: tuple(numpy.ndarray(npix,dtype=np.double),numpy.ndarray(npix,dtype=np.double))
    :raise: HessioGeneralError: when pixel position not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)

    pos_x = np.zeros(npix,dtype=np.double)
    pos_y = np.zeros(npix,dtype=np.double)

    result = lib.get_pixel_position(telescope_id,pos_x,pos_y)
    if result == 0:
        return pos_x, pos_y
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no pixel position for telescope "
                              + str(telescope_id)))


def get_pixel_shape(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: pixels shape for a telescope id
    :rtype: numpy.ndarray(npix,dtype=np.double)
    :raise: HessioGeneralError: when pixel shape not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)

    shape = np.zeros(npix,dtype=np.double)

    result = lib.get_pixel_shape(telescope_id,shape)
    if result == 0:
        return shape
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no pixel position for telescope "
                              + str(telescope_id)))


def get_pixel_area(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: pixels area for a telescope id
    :rtype: numpy.ndarray(npix,dtype=np.double)
    :raise: HessioGeneralError: when pixel area not available for this telescope
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """
    npix = get_num_pixels(telescope_id)

    area = np.zeros(npix,dtype=np.double)

    result = lib.get_pixel_area(telescope_id,area)
    if result == 0:
        return area
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("no pixel position for telescope "
                              + str(telescope_id)))


def get_mc_event_xcore():
    """
    :return: x core position w.r.t. array reference point [m], x -> N
    :rtype: float
    """
    return  lib.get_mc_event_xcore()


def get_mc_event_ycore():
    """
    :return: y core position w.r.t. array reference point [m],y -> W
    :rtype: float
    """
    return  lib.get_mc_event_ycore()


def get_mc_event_offset_fov():
    """
    :return: offset of pointing direction in camera f.o.v. divided by focal length, i.e. converted to radians: [0] = Camera x (downwards in normal pointing, i.e. increasing Alt) [1] = Camera y -> Az.
    :rtype: numpy.ndarray(2,dtype=np.double)
    :raise: HessioGeneralError: when information is not available
    """
    offset = np.zeros(2,dtype=np.double)

    result = lib.get_mc_event_offset_fov(offset)
    if result == 0:
        return offset
    else:
        raise(HessioGeneralError("hsdata is not available"))

def get_mc_number_photon_electron(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: numbers of photon electron
    :rtype: int
    :raise: HessioTelescopeIndexError when no telescope with this id exists
    :raise: HessioGeneralError if hsdata is not available
    """
    npix = get_num_pixels(telescope_id)
    pe = np.zeros(npix,dtype=np.int32)
    result = lib.get_mc_number_photon_electron(telescope_id,pe)
    if result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    elif result < 0:
        raise(HessioGeneralError("numbers of photon electron not available"))
    return pe

def get_mc_shower_energy():
    """
    :return: shower primary energy [TeV]
    :rtype: float
    """
    return  lib.get_mc_shower_energy()


def get_mc_shower_azimuth():
    """
    :return: shower azimuth (N->E) [rad]
    :rtype: float
    """
    return  lib.get_mc_shower_azimuth()


def get_mc_shower_altitude():
    """
    :return: shower altitude [rad]
    :rtype: float
    """
    return  lib.get_mc_shower_altitude()


def get_mc_shower_primary_id():
    """
    :return: shower primary ID 0 (gamma), 1(e-), 2(mu-), 100*A+Z for nucleons and nuclei, negative for antimatter.
    :rtype: int
    """
    return  lib.get_mc_shower_primary_id()


def get_mc_shower_h_first_int():
    """
    :return: shower height of first interaction a.s.l. [m]
    :rtype: float
    """
    return  lib.get_mc_shower_h_first_int()


def get_adc_known(telescope_id, channel, pixel_id):
    """

    :param  telescope_id: telescope's id
    :type telescope_id: int
    :param channel: HI_GAIN, LOW_GAIN
    :type channel: int
    :param pixel_id: pixel's id
    :type pixel_id: int
    :return: individual channel recorded information ? Bit 0: sum, 1: samples, 2: ADC was in saturation.
    :rtype: int
    """
    return lib.get_adc_known(telescope_id, channel, pixel_id)


def get_ref_shape(telescope_id, channel, fshape):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :param channel: HI_GAIN, LOW_GAIN
    :type channel: int
    :param fshape:
    :type fshape: int
    :return:  Reference pulse shape(s) If telescope_id, channel or fshape are not valid return 0.
    :rtype: float
    """
    return lib.get_ref_shape(telescope_id, channel, fshape)


def get_ref_shapes(telescope_id,channel):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :param channel: HI_GAIN, LOW_GAIN
    :type channel: int
    :return: Array of Reference pulse shape(s). 0 if channel is not valid TEL_INDEX_NOT_VALID if telescope index is not valid
    :rtype: numpy.array(num_shapes,dtype=np.double)
    """
    num_shapes= get_lrefshape(telescope_id)
    if  num_shapes>= 0:
        array = np.zeros(num_shapes,dtype=np.double)
        lib.get_ref_shapes(telescope_id, channel, array)
        return array
    else:
        raise(HessioGeneralError("PixelTimming pulse shape(s) not available"))


def get_nrefshape(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return:  Number of following reference pulse shapes (num_gains or 0) TEL_INDEX_NOT_VALID if telescope index is not valid
    :rtype: int
    """
    return lib.get_nrefshape(telescope_id)


def get_lrefshape(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: Length of following reference pulse shape(s). TEL_INDEX_NOT_VALID if telescope index is not valid
    :rtype: int
    """
    return lib.get_lrefshape(telescope_id)


def get_ref_step(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return:  If telescope_id, channel or fshape are not valid return 0.
    :rtype: int
    """
    return lib.get_ref_step(telescope_id)


def get_time_slice(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: Width of readout time slice (i.e. one sample) [ns]. If telescope_id is not valid return 0.
    :rtype: float
    """
    return lib.get_time_slice(telescope_id)


def get_tel_event_gps_time(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: telescope event gps tine in a 2D array: -seconds  -nonosecond
    :rtype: numpy.ndarray(1,dtype=np.long)
    """
    seconds = np.zeros(1,dtype=np.long)
    nanoseconds = np.zeros(1,dtype=np.long)

    result = lib.get_tel_event_gps_time(telescope_id,seconds,nanoseconds)
    if result == 0:
        return seconds[0], nanoseconds[0]
    else:
        raise(HessioGeneralError("no event gps time for telescope "))


def get_central_event_gps_time():
    """
    :return: telescope central envent gps tine in a 2D array: -seconds  -nonosecond
    :rtype: numpy.ndarray(1,dtype=np.long)
    """
    seconds = np.zeros(1,dtype=np.long)
    nanoseconds = np.zeros(1,dtype=np.long)

    result = lib.get_central_event_gps_time(seconds,nanoseconds)
    if result == 0:
        return seconds[0], nanoseconds[0]
    else:
        raise(HessioGeneralError("no central event  gps time"))


def get_central_event_teltrg_list():
    """
    :return: List of IDs of triggered telescopes
    :rtype: np.ndarray(num_teltrig,dtype=np.int32)
    :raise: HessioGeneralError: when information is not available
    """
    num_teltrig= lib.get_num_tel_trig()
    if num_teltrig >= 0:
        array = np.zeros(num_teltrig,dtype=np.int32)
        lib.get_central_event_teltrg_list(array)
        return array
    else:
        raise(HessioGeneralError("hsdata is not available"))


def get_camera_rotation_angle(telescope_id):
    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: rotation angle of the camera of a given telescope (counter-clock-wise from back side for prime focus camera)L
    :rtype: float
    :raise: HessioGeneralError: when hsdata->camera_set[itel].cam_rot not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """

    result = lib.get_camera_rotation_angle(telescope_id)
    if result >=0 : return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->camera_set[itel].cam_rot not available"))


def get_mirror_number(telescope_id):

    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: total number of mirror tiles of a telescope
    :rtype: int
    :raise: HessioGeneralError: when hsdata->camera_set[itel].num_mirrors not available
    :raise: HessioTelescopeIndexError when no telescope exist with this id
    """
    result = lib.get_mirror_number(telescope_id)
    if result >= 0 : return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->camera_set[itel].num_mirrors not available"))


def get_optical_foclen(telescope_id):

    """
    :param  telescope_id: telescope's id
    :type telescope_id: int
    :return: focal length of optics of a telescope [m]
    :rtype: float
    :raise: HessioGeneralError: when hsdata->camera_set[itel].flen not available
    :raise: HessioTelescopeIndexError: when no telescope exist with this id
    """

    result = lib.get_optical_foclen(telescope_id)
    if result >= 0 : return result
    elif result == TEL_INDEX_NOT_VALID:
        raise(HessioTelescopeIndexError("no telescope with id " + str(telescope_id)))
    else:
        raise(HessioGeneralError("hsdata->camera_set[itel].flen not available"))


def get_telescope_ids():
    """
    :return: list of IDs of telescopes used in the run
    :rtype: numpy.ndarray(num_tel,dtype=np.int32)
    :raise: HessioGeneralError: when information is not available
    """
    num_tel = get_num_telescope()
    if num_tel >= 0:
        array = np.zeros(num_tel,dtype=np.int32)
        lib.get_telescope_ids(array)
        return array
    else:
        raise(HessioGeneralError("hsdata->run_header.tel_id is not available"))
