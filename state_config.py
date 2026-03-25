"""
State configuration for this ConnecticutDischargeWatch instance.

All state-specific values are centralized here. To deploy for a new state,
run: python deploy_new_state.py <STATE_CODE>

This file is overwritten by deploy_new_state.py — do not add logic here.
"""

STATE_CODE = "CT"
STATE_NAME = "Connecticut"
APP_NAME = "ConnecticutDischargeWatch"
APP_TAGLINE = "Connecticut Discharge Monitoring"
DOMAIN = "connecticutdischargewatch.org"
DATA_FILE = "ct_exceedances_launch_ready.csv"
CONTACT_EMAIL = "data@connecticutdischargewatch.org"
MAILING_ADDRESS = ""
TIMEZONE_LABEL = "EST"
EPA_REGION = 1
