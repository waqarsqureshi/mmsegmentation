import os.path as osp

from .builder import DATASETS
from .custom import CustomDataset

@DATASETS.register_module()
class RoadSurveyDataset(CustomDataset):

    """RoadSurveyDataset

    The ``img_suffix`` is fixed to '.jpg' and ``seg_map_suffix`` is
    fixed to '.png for RoadSurvey dataset. 0 is the ignore index.
    ``reduce_zero_label`` should be set to FALSE
    """
    #CLASSES = ('EMPTY','BACKGROUND', 'ROAD', 'SKY', 'SIDEWALK')
    CLASSES = ('BACKGROUND', 'HUMAN', 'POLE','ROAD','TRAFFIC LIGHT','TRAFFIC SIGN','VEHICLE')
   
    #PALETTE = [[0, 0, 0],[128, 0, 0],[0, 128, 0],[128,128, 0],[ 0, 0,128]]
    PALETTE = [[ 0, 0, 0],[220,20,60],[153,153,153],[128,64,128],[250,170,30],[220,220,0],[0,0,142]]
    def __init__(self, **kwargs):
        super(RoadSurveyDataset, self).__init__(
            img_suffix='_leftImg8bit.jpg',
            seg_map_suffix='_gtFine_labelIds.png',
            reduce_zero_label=False,
            **kwargs)