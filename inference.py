import os
import random
from uuid import uuid4
import time

from gevent import monkey

monkey.patch_all()

from comet_mpm import CometMPM

enabledMPM = False

if os.getenv("COMET_MPM", "") != "":
    enabledMPM = True

MPM = CometMPM(
    api_key=os.getenv("COMET_API_KEY", "COMET_API_KEY"),
    workspace_name="knock",
    model_name="ai-email-nnet-bnorm",
    model_version="1.0.0",
    disabled=not enabledMPM,
)

print(f"MPM enabled {enabledMPM}")

# Force the MPM SDK to send everything
for i in range(500):
    prediction_id = str(uuid4())
    MPM.log_event(prediction_id=prediction_id, output_value=0)
    MPM.log_event(prediction_id=prediction_id, input_features={"age": 32})
    print("Prediction id", prediction_id)


time.sleep(1)
