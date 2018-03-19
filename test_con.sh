DE="ba5b5824.ngrok.io"
curl -s -X POST -k --data @- http://${DE}/resources/json/delphix/session \
    -c ~/cookies.txt -H "Content-Type: application/json" <<EOF
{
    "type": "APISession",
    "version": {
        "type": "APIVersion",
        "major": 1,
        "minor": 8,
        "micro": 2
    }
}
EOF