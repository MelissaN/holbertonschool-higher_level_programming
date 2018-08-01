#!/bin/bash
# Take in URL, send DELETE request, display response body; Usage: ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
curl -sX DELETE "$1"
