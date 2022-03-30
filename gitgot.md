# Missing Fox

Note: If the person that figured out the second part to this question is reading this please contact me, I'd love to hear the solution

# GitGot

![img](https://lh4.googleusercontent.com/JqJLNMiP6EpNt-BXE9rYdxSWDp9zIdhC5YDbGdUSHzPUSIgkdx2307xHBsVev4dN94rWseHv0ZTYQ6ddkMhBjuzENsMhNJWTwEtiJehNvQLO1kBd5FUuNg_1Zb5li2ChhE5t-M07)

This was hard but super cool

I've included the files with the tool already downloaded in this repository if anyone wants to try it

So the first thing I did was look through the files we were given, we have a GadetProbe file and a GitGot file

GadetProbe had a wordlists file which I didn't really understand

There was also python file, a java file, and a jar file

GitGot has visibly a json file (the GitGot file was an additional file I downloaded and added which I'll get to later)

GitGot also has a hidden .bash_history file (which has the most recent commands run)

Finding this hidden file is the key to this problem

I ran the commands with indexes 1970, 1971, 1972, and 1973 to install and insert the necessary github key for the program to run

The python file basically searches through github repositories for a certain list of criteria

After getting gitgot setup I simply ran the last command listed in index 1974

python3 gitgot.py --gist -q 'firefox "main.js" filename:"js"' -r ../gitgot_saved_state.json

Running this command will search it through the first till it finds the first match

It took me a few searches to be able to find the correct result, I was really worried I was going to skip it but the correct one is fairly obvious

The flag is in plaintext

**Flag Repository No Longer Up**

Unfortunately it looks like they took the repository down so you won't be able to get the flag yourself

The flag was in plaintext near the top in a comment with the format flag{}