//SPDX-Licence-Identifier: MIT
pragma solidity 0.8.19;

import "../node_modules/@openzeppelin/contracts/access/AccessControl.sol";

contract RightfulShare is AccessControl {

    bytes32 public constant ADMIN_ROLE = 0x00;
    bytes32 public constant GBH_ROLE = keccak256("GBH_ROLE");
    bytes32 public constant CONTRIBUTER_ROLE = keccak256("CONTRIBUTER_ROLE"); // seperate this functionality out?

    mapping(address => uint) public ids;

    uint public latestId = 0; // id 0 is erserved as error indicator

    function addMember(address _address) onlyRole(ADMIN_ROLE) public returns(uint id) {
        require(ids[_address] == 0, "already member");
        latestId += 1;
        ids[_address] = latestId;
        return latestId;
    }

}