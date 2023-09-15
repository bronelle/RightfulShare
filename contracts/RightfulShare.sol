//SPDX-Licence-Identifier: MIT
pragma solidity 0.8.19;

import "../node_modules/@openzeppelin/contracts/access/AccessControl.sol";

contract RightfulShare {

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