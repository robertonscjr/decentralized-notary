pragma solidity ^0.4.0;

contract NotaryOffice {
    struct Document {
        address owner;
        bool verified;
    }
    
    mapping(bytes32 => Document) public registeredDocuments;
    address public notaryAddress;
    
    event DocumentRegistered(bytes32 documentHash, address owner);
    function registerDocument(bytes32 documentHash) public payable {
        registeredDocuments[documentHash] = Document({owner: msg.sender,
													  verified: false});

        emit DocumentRegistered(documentHash, msg.sender);
    }
    
    event DocumentValidated(bytes32 documentHash, address owner, address notary);
    function validateDocument(bytes32 documentHash) public {
        require(msg.sender == notaryAddress);
        registeredDocuments[documentHash].verified = true;
        emit DocumentValidated(documentHash, registeredDocuments[documentHash].owner,
			                   notaryAddress);
    }
    
}
