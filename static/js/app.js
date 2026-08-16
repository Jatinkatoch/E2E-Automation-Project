document.addEventListener("DOMContentLoaded", function () {


    // Product Search

    const search = document.getElementById("search");


    if (search) {


        search.addEventListener("keyup", function () {


            const value = this.value.toLowerCase();


            document.querySelectorAll(".product").forEach(function(card){


                const text = card.innerText.toLowerCase();


                if(text.includes(value)){

                    card.style.display="block";

                }
                else{

                    card.style.display="none";

                }


            });


        });


    }




    // Category Filter


    const buttons = document.querySelectorAll(".filter");


    buttons.forEach(function(button){


        button.addEventListener("click",function(){


            const category = this.dataset.category;



            document.querySelectorAll(".product").forEach(function(card){



                if(
                    category === "all" ||
                    card.dataset.category === category
                )
                {

                    card.style.display="block";

                }
                else
                {

                    card.style.display="none";

                }


            });



        });


    });



});