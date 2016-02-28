//TODO - commented these lines because they seem to break the script.
//Fix this if they are necessary


// external js: masonry.pkgd.js

// var grid = document.querySelector('.grid');
// var msnry = new Masonry(grid, {
//   columnWidth: 100
//   gutter: 10

// });

// grid.addEventListener('click', function(event) {
//   // don't proceed if item was not clicked on
//   if (!matchesSelector(event.target, '.grid-item')) {
//     return;
//   }
//   // change size of item via class
//   event.target.classList.toggle('grid-item--gigante');
//   // trigger layout
//   msnry.layout();
// });






//Sam's code
// <script>
//Set the large image to the selected image
function setImgEltsStyle()
{
    for (var i=0; i<list.length; i++)
        list[i].style.border = "";

    list[listIndex].style.border="5px solid red";

    console.log(listIndex);

    var putImageHere = document.getElementsByClassName("grid-large-image");
    
    //TODO
    //This is where we set the image to whatever the value is in the small rectangle
    putImageHere[0].style.content = "url(http://placehold.it/350x100)";

    //list[listIndex].src;
}




// Store frame for motion functions
var previousFrame = null;

//If we had a gesture in the last 500 ms don't allow another
var recentGesture = false;
var recentGestureTimeLimit = 500;
function flipRecentGesture()
{
    recentGesture = !recentGesture;
}

//Get all img elements on page
// var list = document.getElementsByTagName("img");
var list = document.getElementsByClassName("grid1").item(0).getElementsByClassName("grid-item")
var listIndex = 0;


//Set first image to "selected"
setImgEltsStyle();


//Enable gestures, duh
var controllerOptions = {enableGestures: true};

// Setup Leap loop with frame callback function
Leap.loop(controllerOptions, function(frame) {


    // Frame motion factors
    if (previousFrame && previousFrame.valid) { 
        var translation = frame.translation(previousFrame);
    }

    var gestureString = "";
    for (var i = 0; i < frame.gestures.length && !recentGesture; i++) {
        var gesture = frame.gestures[i];
        
        //Set the recentGesture var to true so and then flip it back
        //after a timeout. This prevents gestures during the timeout.
        flipRecentGesture();
        setTimeout(flipRecentGesture, recentGestureTimeLimit);


        //Perform different actions based on the gesture type
        switch (gesture.type) {

            case "circle":
                console.log("gesture: circle");
              break;

            case "swipe":
                //If swipe right
                if (translation[0] >= 0)
                {
                    listIndex++;
                    if ( listIndex >= list.length)
                        listIndex=0;
                }
                //If swipe left
                else
                {
                    listIndex--;
                    if ( listIndex < 0)
                        listIndex = list.length-1;
                }
                setImgEltsStyle();
              
                console.log("gesture: swipe");
              break;

            case "screenTap":
            case "keyTap":

              console.log("gesture: tap");
            break;

            default:
          }
        }

    // Store frame for motion functions
    previousFrame = frame;
})

// </script>