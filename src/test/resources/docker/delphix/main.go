package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"github.com/gorilla/mux"
)


// Release struct used to return json after createRelease is called
type DelphixResponse struct {
	DelphixID string `json:"delphixId"`
	Status    string `json:"status"`
}

func main() {
	router := mux.NewRouter().StrictSlash(true)
	router.HandleFunc("/resources/json/delphix/database/{ref_id}/refresh", ReturnDatabaseRefreshResponse).Methods("POST")

	router.HandleFunc("/resources/json/delphix/login", ReturnLoginResponse).Methods("POST")

	router.HandleFunc("/resources/json/delphix/selfservice/bookmark", ReturnBookmarkResponse).Methods("GET")
	router.HandleFunc("/resources/json/delphix/selfservice/template", ReturnTemplateResponse).Methods("GET")
	

	router.HandleFunc("/resources/json/delphix/session", ReturnSessionResponse).Methods("POST")
	
	log.Fatal(http.ListenAndServe(":8080", router))
}

// ReturnDatabaseRefreshResponse sends a dummy response back
func ReturnDatabaseRefreshResponse(res http.ResponseWriter, req *http.Request) {
	res.Header().Set("Content-Type", "application/json")
	b := json.RawMessage(`{
		"type":"OKResult",
		"status":"OK",
		"result": "",
		"job":null,
		"action":null
	}`)
	res.WriteHeader(http.StatusOK)
	fmt.Fprint(res, string(b))
}

// ReturnLoginResponse sends a dummy response back
func ReturnLoginResponse(res http.ResponseWriter, req *http.Request) {
	res.Header().Set("Content-Type", "application/json")
	b := json.RawMessage(`{
		"status":"OK",
		"type": "OKResult",
		"result":"USER-2",
		"job":null,
		"action":null
		}`)
	res.WriteHeader(http.StatusOK)
	fmt.Fprint(res, string(b))
}

// ReturnBookmarkResponse sends a dummy response back
func ReturnBookmarkResponse(res http.ResponseWriter, req *http.Request) {
	res.Header().Set("Content-Type", "application/json")
	b := json.RawMessage(`{
		"type":"OKResult",
		"status":"OK",
		"result": "",
		"job":null,
		"action":null
	}`)
	res.WriteHeader(http.StatusOK)
	fmt.Fprint(res, string(b))
}

// ReturnTemplateResponse sends a dummy response back
func ReturnTemplateResponse(res http.ResponseWriter, req *http.Request) {
	res.Header().Set("Content-Type", "application/json")
	b := json.RawMessage(`{
		"type":"OKResult",
		"status":"OK",
		"result": "",
		"job":null,
		"action":null
	}`)
	res.WriteHeader(http.StatusOK)
	fmt.Fprint(res, string(b))
}

// ReturnSessionResponse sends a dummy response back
func ReturnSessionResponse(res http.ResponseWriter, req *http.Request) {
	res.Header().Set("Content-Type", "application/json")
	b := json.RawMessage(`{
		"status": "OK",
		"type": "OKResult",
		"result":{
			"type":"APISession",
			"version":{
				"type":"APIVersion",
				"major":1,
				"minor":7,
				"micro":0
			},
			"locale":null,
			"client":null
		},
		"job":null
	}`)
	res.WriteHeader(http.StatusOK)
	fmt.Fprint(res, string(b))
}
