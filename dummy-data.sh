# Create some dummy data for demo

# Environments
curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "production01",
    "group": "myGroup",
    "location": "Azure-UKSouth",
    "description": "The main production environment used for most of our services",
    "version": "2.3.1"
}'

curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "production02",
    "group": "myGroup",
    "location": "Azure-UKWest",
    "description": "The backup production environment used for distaster recovery",
    "version": "2.3.0"
}'

curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "staging01",
    "group": "myGroup",
    "location": "Azure-UKSouth",
    "description": "The staging environment used for pre-live tests and proving",
    "version": "2.3.1"
}'

curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "staging02",
    "group": "myGroup",
    "location": "Azure-UKSouth",
    "description": "The staging environment used for pre-live DR tests",
    "version": "2.3.0"
}'

curl --location --request POST 'http://127.0.0.1:8000/api/environments/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "development01",
    "group": "myGroup",
    "location": "Azure-UKSouth",
    "description": "The development environment",
    "version": "2.3.2"
}'

# Clusters
curl --location --request POST 'http://127.0.0.1:8000/api/clusters/' \
--header 'Authorization: Basic YWRtaW46YWRtaW4=' \
--header 'Content-Type: application/json' \
--header 'Cookie: csrftoken=3puWbsMc3aUwzqmmoZ6B25d5LqAwwxyC177x3oOfBM0LHwyFcjij7AAIAaU3vDR3' \
--data-raw '{
    "title": "aks-k8s-001",
    "type": "kubernetes",
    "description": "The main production kubernetes cluster",
    "environment": "http://127.0.0.1:8000/api/environments/1/",
    "version": "1.12.1"
}'