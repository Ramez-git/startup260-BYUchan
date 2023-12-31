import os

directory_path = './pages'

for filename in os.listdir(directory_path):
    if filename == "mass.py" or filename[-1]=="g":
        continue
    else:
        with open(f"{directory_path}/{filename}",'w') as file:
            filename=filename[:len(filename)-5]
            htmlcode=f"""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>BYUchan</title>
        <link rel="icon" type="image/x-icon" href="../icon.png">
        <body>
            <header>
                <image src="{filename}.png" width="200" hight="200"></image>
                <h1><a href="../index.html">&larr;</a> {filename} Room<sup>&Yopf;</sup></h1>
        </head>
        <body>
            <button id="showFormButton">Start a thread</button>
            <form id="start a thread">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" placeholder="anonymous"><br><br>
            
                <label for="Subject">Subject</label>
                <input type="Subject" id="Subject" name="Subject"><br><br>
                <label for="comments">Comments</label>
                <textarea id="comments" name="comments" rows="4" cols="50"></textarea>

                <button>add images</button>
                <input type="submit" value="Submit">
            </form>
            
            <script>
                // JavaScript to toggle the form's visibility
                document.getElementById('showFormButton').addEventListener('click', function() {{
                    var form = document.getElementById('submissionForm');
                    if (form.style.display === 'none' || form.style.display === '') {{
                        form.style.display = 'block';
                    }} else {{
                        form.style.display = 'none';
                    }}
                }});
            </script>
            <hr>
            <h2>Threads</h2>
            <footer>
                <hr />
                  <span class="text-reset">Ramez Gammoh</span>
                  <br />
                  <a href="https://github.com/Ramez-git/startup260-BYUchan">GitHub</a>
            </footer>
        </body>
</html>
"""
            file.write(htmlcode)
        