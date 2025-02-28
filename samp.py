import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import cv2


import numpy as np
import mediapipe as mp
import math
import av
from tensorflow.keras.models import Model
from tensorflow.keras.layers import (LSTM, Dense, Dropout, Input, Flatten, 
                                     Bidirectional, Permute, multiply)