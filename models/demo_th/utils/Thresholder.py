from mhubio.core import Module, Instance, InstanceData, IO
from segdb.classes.Segment import Segment

# register custom segmentation before class definition
Segment.register("THRESHOLDED", name="Thresholded", color=(255, 0, 0))

@IO.Config('lower', int, 0, the='lower threshold')
@IO.Config('upper', int, 0, the='upper threshold')
class Thresholder(Module):
    
    lower: int
    upper: int

    @IO.Instance()
    @IO.Input('image', 'nifti:mod=ct',  the='input ct scan')
    @IO.Output('thresholded', 'thresholded.nii.gz', 'nifti:mod=seg:model=demo_th:roi=THRESHOLDED', the='thresholded image')
    def task(self, instance: Instance, image: InstanceData, thresholded: InstanceData) -> None:

        # build cli command for thresholder
        cmd = [
          'thresholder',
          '--input', image.abspath,
          '--output', thresholded.abspath,
          '--lower', str(self.lower),
          '--upper', str(self.upper)
        ]
        
        # debug message
        self.log.debug('Running command: %s', ' '.join(cmd))

        
        # run command
        self.subprocess(cmd)