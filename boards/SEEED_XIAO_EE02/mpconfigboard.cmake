include(boards/SEEED_XIAO_ESP32S3/mpconfigboard.cmake)

# list(APPEND SDKCONFIG_DEFAULTS
#    boards/SEEED_XIAO_EE02/sdkconfig.board
# )

set(MICROPY_FROZEN_MANIFEST ${MICROPY_BOARD_DIR}/manifest.py)
