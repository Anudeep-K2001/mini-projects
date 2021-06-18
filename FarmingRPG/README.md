# Term Paper

Unity is a game engine which has so many built in features like physics engine, collider system, 3D and 2D support and so on.
Unity also supports VR.

Even though unity is mainly aimed for gaming, Simulations for AI can be done using Unity in a very efficient way.


## Part 1

In this project, Our goal is to make  a 2D game which is a basic farming game.

For any game, there must be a player character. And in this project, this is our main character.

![image](https://user-images.githubusercontent.com/50168940/122519842-8a2acb00-d030-11eb-847b-de595c7184ad.png)

This is our main character and we call him Player.

As every game goes, there should be only one player. So in unity we use singletonMonobehaviour to avoid duplicates.
It's demonstration looks as follows

![SingletonMonoBehaviour](https://user-images.githubusercontent.com/50168940/122520909-d62a3f80-d031-11eb-935e-cc6a8f4e0506.gif)



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


    }
```
    
The above code will control player movement.
``` yInput = Input.GetAxisRaw("Vertical"); ```
This gets input from keyboard on vertical axis.


We have added movement to our player and lets see how it looks

![Movement](https://user-images.githubusercontent.com/50168940/122520414-3076d080-d031-11eb-8090-f9c2f85ecbdc.gif)

We have given movement and player input to player but it doesn't look natural.
So let's add some animation to make it look more like a player.

![image](https://user-images.githubusercontent.com/50168940/122520675-8b102c80-d031-11eb-8ae5-9bee00d59c75.png)

Now that we have added animation, let's see how it looks

![PlayerMovement and Animation](https://user-images.githubusercontent.com/50168940/122520949-e0e4d480-d031-11eb-8ece-1b90d80b2c87.gif)

And it looks very decent now.


## Part 2

As of now, we have worked on player and his movement but there wont be much to do if there is no Map to explore.
So let's make a map for player to roam.

![image](https://user-images.githubusercontent.com/50168940/122521773-d971fb00-d032-11eb-9c47-ffda1ba9d936.png)

This the map we created using tilemaps feature present in Unity.
Looking deeper into it, we have few layers in it and these layers are called sorting layers.
They decide how the image must be drawn and sets the order of drawing.

![image](https://user-images.githubusercontent.com/50168940/122521796-e0990900-d032-11eb-8bdd-23e4c6e15b9f.png)

As you can see, there are multiple layers, in this `Ground1` is drawn first and then followed by `Ground2` and so on.
We can see there is a layer called collisions, this layer holds the properties of collisions and this interacts with player's collider.

![image](https://user-images.githubusercontent.com/50168940/122522367-86e50e80-d033-11eb-9b4e-49804bddaf65.png)

as you can see the blue area in the map is the collision area where the player cannot pass through.

and thats how a basic map is created.


## Part 3





