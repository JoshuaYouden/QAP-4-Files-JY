// Script is for a Motel customer
// Author: Joshua Youden
// Last edited: March 24th, 2024

// Object Literals
const customer = {
  firstName: "John",
  lastName: "Mclain",
  date_Of_Birth: "1992-02-25",
  gender: "male",
  room_Prefrences: ["Double bed", "Pet-friendly"],
  pay_Method: "cash",
  address: {
    mailing_Address: "22 Vexen Lane",
    city: "Thompson",
    province: "CH",
  },
  phone_Number: "709-596-4389",
  check_In_Out: {
    check_In: "2024-02-12",
    check_Out: "2024-02-18",
  },
  getAge: function () {
    const today = new Date();
    const birth_Date = new Date(this.date_Of_Birth);
    let age = today.getFullYear() - birth_Date.getFullYear();
    const m = today.getMonth() - birth_Date.getMonth();
    if (m < 0 || (m === 0 && today.getDate() < birth_Date.getDate())) {
      age--;
    }
    return age;
  },
  newDate: function () {
    this.check_In = new Date(this.check_In_Out.check_In);
    this.check_Out = new Date(this.check_In_Out.check_Out);
    this.difference_In_Stay =
      this.check_Out.getDate() - this.check_In.getDate();
    this.duration_of_Stay = Math.round(
      this.difference_In_Stay / (1000 * 3600 * 24)
    );
  },
  getDescription: function () {
    return `Hello, my name is ${customer.firstName}. I am ${peep} years old ${customer.gender} who perfers rooms with a ${customer.room_Prefrences[0]} and ${customer.room_Prefrences[1]} status. You can reach me at ${customer.phone_Number}. My address is ${customer.address.mailing_Address}, ${customer.address.city}, ${customer.address.province}. I will be staying from ${customer.check_In_Out.check_In} to ${customer.check_In_Out.check_Out}, which is a duration of ${customer.difference_In_Stay} days.`;
  },
};

customer.newDate();

let peep = customer.getAge();
console.log(
  `Hello, my name is ${customer.firstName} ${customer.lastName}. I am a ${peep} year old ${customer.gender} who prefers rooms with a ${customer.room_Prefrences[0]} and a ${customer.room_Prefrences[1]} status. You can reach me at ${customer.phone_Number}. My address is ${customer.address.mailing_Address}, ${customer.address.city}, ${customer.address.province}. I will be staying from ${customer.check_In_Out.check_In} to ${customer.check_In_Out.check_Out}, which is a duration of ${customer.difference_In_Stay} days.`
);
