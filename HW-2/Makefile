all: minikube/start deploy get_ip

clean: destroy/all minikube/destroy

minikube/start:
	minikube start

minikube/stop:
	minikube start

minikube/destroy:
	minikube delete

get_ip:
	kubectl get nodes -o wide

deploy:
	kubectl apply -f "*.yaml"

destroy/all:
	kubectl delete -f "*.yaml"

destroy/deploy:
	kubectl delete -f "*deployment.yaml"

