<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Online Dictionary</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f8f9fa;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }

        .search-container {
            max-width: 600px;
            width: 100%;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0px 0px 15px rgba(0, 0, 0, 0.1);
        }

        .search-bar {
            display: flex;
            align-items: center;
        }

        .search-bar input {
            flex: 1;
            padding: 10px;
            border: 1px solid #ced4da;
            border-radius: 5px;
        }

        .search-bar button {
            margin-left: 10px;
            padding: 10px 15px;
            border: none;
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            cursor: pointer;
        }

        .search-bar button:hover {
            background-color: #0056b3;
        }

        .microphone-icon {
            margin-left: 10px;
            font-size: 1.5em;
            cursor: pointer;
        }

        .results {
            margin-top: 20px;
        }
    </style>
</head>

<body>
    <div class="search-container">
        <h2 class="text-center">Online Dictionary</h2>
        <div class="search-bar">
            <input type="text" id="searchWord" placeholder="Enter a word...">
            <button id="searchButton">Search</button>
            <span class="microphone-icon" onclick="startVoiceSearch()">🎤</span>
        </div>
        <div class="results" id="results">
            <!-- Results will be displayed here -->
        </div>
    </div>

    <script>
        function startVoiceSearch() {
            // Placeholder function for voice search
            alert("Voice search feature is not yet implemented.");
        }

        document.getElementById('searchButton').addEventListener('click', function () {
            const word = document.getElementById('searchWord').value;
            if (word) {
                searchWord(word);
            }
        });

        function searchWord(word) {
            // Placeholder for the function to search for a word definition.
            // This should connect to the backend using Python & Google Speech Recognition.
            document.getElementById('results').innerHTML = `<p>Searching for: <strong>${word}</strong></p>`;
        }
    </script>
</body>

</html>
