#!/bin/sh
# Zet de apparatenlijsten uit .env om naar het formaat dat Telegraf in telegraf.conf verwacht.
# Zo staat elk apparaat op één plek (.env) en hoef je telegraf.conf nooit aan te passen.
set -eu

# Maakt van "a,b" de tekst ["<voor>a<na>","<voor>b<na>"].
maak_lijst() {
  lijst="$1"
  voor="$2"
  na="$3"
  resultaat=""
  oud=$IFS
  IFS=,
  for item in $lijst; do
    item=$(printf '%s' "$item" | tr -d ' \r')
    [ -n "$item" ] && resultaat="${resultaat}\"${voor}${item}${na}\","
  done
  IFS=$oud
  printf '[%s]' "${resultaat%,}"
}

SNMP_AGENTS=$(maak_lijst "${SNMP_APPARATEN:?Zet SNMP_APPARATEN in .env}" "udp://" ":161")
PING_URLS=$(maak_lijst "${PING_DOELEN:?Zet PING_DOELEN in .env}" "" "")
export SNMP_AGENTS PING_URLS

echo "SNMP-apparaten: ${SNMP_AGENTS}"
echo "Pingdoelen: ${PING_URLS}"

exec telegraf
