class Node{
	int data;
	Node* nextNode;
	Node(int data, Node* newNode){
		data = 0;
		nextNode = newNode;
	}
	Node(Node*original){
		data = original->getData();
		nextNode = original->getNextNode();
	}
	void main(){

	}
	int getData(){
		return data;
	}
	Node* getNextNode(){
		return nextNode;
	}
};