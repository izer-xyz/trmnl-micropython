include(boards/SEEED_XIAO_ESP32S3/mpconfigboard.cmake)

list(APPEND SDKCONFIG_DEFAULTS
   ${MICROPY_BOARD_DIR}/sdkconfig.board
)

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)
