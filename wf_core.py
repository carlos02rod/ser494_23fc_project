#ill call wf_dataprocessing to process data followed by wf_visualization
#to generate the statistics and visuals

import wf_dataprocessing
import wf_visualization

if __name__ == "__main__":
    wf_dataprocessing.run()
    wf_visualization.run()
