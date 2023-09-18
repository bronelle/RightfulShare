//SPDX-Licence-Identifier: MIT
pragma solidity 0.8.19;

import "../node_modules/@openzeppelin/contracts/access/AccessControl.sol";

contract RightfulShare is AccessControl {

    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE"); // Should use default admin role? 0x00
    bytes32 public constant GBH_ROLE = keccak256("GBH_ROLE");
    bytes32 public constant CONTRIBUTER_ROLE = keccak256("CONTRIBUTER_ROLE"); // seperate this functionality out?

    mapping(address => uint) public ids;

    uint public latestId = 0; // id 0 is erserved as error indicator

    function addMember(address _address) public returns(uint id) {
        // only admin
        // require doesn't exist already
        latestId += 1;
        ids[_address] = latestId;
        return latestId;
    }

}