function dropHandler(event) {
    event.preventDefault();

    if (event.dataTransfer.items) {
        var fileInput = document.getElementById('file-input');
        var totalFiles = fileInput.files.length + event.dataTransfer.items.length;

        if (totalFiles > 10) {
            alert('You can only upload 10 files.');
            return;
        }

        for (var i = 0; i < event.dataTransfer.items.length; i++) {
            if (event.dataTransfer.items[i].kind === 'file') {
                var file = event.dataTransfer.items[i].getAsFile();

                // Validate and display images
                validateAndDisplayImages(file);
            }
        }
    }
}

function dragOverHandler(event) {
    event.preventDefault();
}

function clickInput() {
    document.getElementById('file-input').click();
}

function validateAndDisplayImages(input) {
    var files;

    if (input instanceof FileList) {
        files = input;
    } else if (input instanceof File) {
        files = [input];
    } else if (input.files instanceof FileList) {
        files = input.files;
    } else {
        console.error('This is an unknown file type.');
        return;
    }

    for (var i = 0; i < files.length; i++) {
        var file = files[i];
        if (file instanceof File && file.type && file.type.startsWith('image/')) {
            displayImage(file);
            updateInput(file);
        } else {
            alert('The selected file is not an image.');
            // Add handling for non-image files if needed
        }
    }
}

function displayImage(file) {
    var imageContainer = document.getElementById('image-container');

    var imgWrapper = document.createElement('div');
    imgWrapper.className = 'image-preview';

    var img = document.createElement('img');
    img.src = URL.createObjectURL(file);

    var deleteButton = document.createElement('span');
    deleteButton.className = 'material-symbols-outlined';
    deleteButton.innerHTML = 'cancel';
    deleteButton.onclick = function () {
        // Remove the preview and the file from the input when the delete button is clicked
        imgWrapper.remove();
        removeImageFromInput(file);
    };

    imgWrapper.appendChild(img);
    imgWrapper.appendChild(deleteButton);
    imageContainer.appendChild(imgWrapper);
}

function updateInput(file) {
    var fileInput = document.getElementById('file-input');

    var fileList = fileInput.files || [];

    var dataTransfer = new DataTransfer();
    for (var i = 0; i < fileList.length; i++) {
        dataTransfer.items.add(fileList[i]);
    }
    dataTransfer.items.add(file);

    fileInput.files = dataTransfer.files;
}

function removeImageFromInput(file) {
    var fileInput = document.getElementById('file-input');
    var fileList = fileInput.files || [];

    var newFileList = Array.from(fileList).filter(function (item) {
        return item !== file;
    });

    var dataTransfer = new DataTransfer();
    for (var i = 0; i < newFileList.length; i++) {
        dataTransfer.items.add(newFileList[i]);
    }

    fileInput.files = dataTransfer.files;
}
