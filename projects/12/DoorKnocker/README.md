docker run --name doorknocker -p 4567:4567 markw/doorknocker:latest

docker run --name doorknocker -p 4567:4567 markw/doorknocker:latest


curl -d '{"query": "select x where y", "requester": "markw"}' http://localhost:4567/knockknock
