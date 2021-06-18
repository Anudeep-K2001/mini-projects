# Term Paper

Unity is a game engine which has so many built in features like physics engine, collider system, 3D and 2D support and so on.
Unity also supports VR.

Even though unity is mainly aimed for gaming, Simulations for AI can be done using Unity in a very efficient way.


In this project, Our goal is to make  a 2D game which is a basic farming game.

For any game, there must be a player character. And in this project, this is our main character.
![image](https://user-images.githubusercontent.com/50168940/122519842-8a2acb00-d030-11eb-847b-de595c7184ad.png)
This is our main character and we call him Player.

We made a character but it wont be interesting unless it can move. So lets add an input system to it.
```
private void PlayerMovementInput()
    {
        yInput = Input.GetAxisRaw("Vertical");
        xInput = Input.GetAxisRaw("Horizontal");

        if(yInput != 0 && xInput != 0)
        {
            xInput = xInput * 0.71f;
            yInput = yInput * 0.71f;
        }

        if(xInput != 0 || yInput != 0)
        {
            isRunning = true;
            isWalking = false;
            isIdle = false;

            movementSpeed = Settings.walkingSpeed;

            if(xInput < 0)
            {
                playerDirection = Direction.left;
            }
            else if(xInput > 0)
            {
                playerDirection = Direction.right;
            }
            else if(yInput < 0)
            {
                playerDirection = Direction.down;
            }
            else
            {
                playerDirection = Direction.up;
            }

        }

        else if (xInput == 0 && yInput == 0)
        {
            isRunning = false;
            isWalking = false;
            isIdle = true;
        }


    }```
    
The above code will control player movement.



![Movement](https://user-images.githubusercontent.com/50168940/122518925-7b8fe400-d02f-11eb-97a7-a8515ba0638f.gif)
