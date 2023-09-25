//SPDX-Licence-Identifier: MIT
pragma solidity 0.8.19;

import "../node_modules/@openzeppelin/contracts/access/AccessControl.sol";

contract RightfulShare is AccessControl {

    bytes32 public constant ADMIN_ROLE = 0x00;
    bytes32 public constant GBH_ROLE = keccak256("GBH_ROLE");
    bytes32 public constant CONTRIBUTER_ROLE = keccak256("CONTRIBUTER_ROLE"); // seperate this functionality out?

    enum Frequency {
        monthly,
        weekly,
        daily,
        biweekly,
        annually
    }

    struct Pool {
        uint totalAmount;
        address[] recipients;
        uint paymentAmount;
        Frequency frequency;
        bool approved;
    }

    mapping(address => uint) public ids;
    Pool[] pools;

    uint public latestId = 0; // id 0 is erserved as error indicator

    function addMember(address _address) onlyRole(ADMIN_ROLE) public returns(uint id) {
        require(ids[_address] == 0, "already member");
        latestId += 1;
        ids[_address] = latestId;
        return latestId;
    }

    /*
    functions:
    */

    function nominatePool() onlyRole(ADMIN_ROLE) public returns (uint id) {

    }

    function approvePool() onlyRole(ADMIN_ROLE) public returns (bool approved) {
        
    }

    function editMember() onlyRole(ADMIN_ROLE) public returns (uint id) {

    }

}