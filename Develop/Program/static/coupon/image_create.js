function dropHandler(event) {
    event.preventDefault();

    if (event.dataTransfer.items) {
        var fileInput = document.getElementById('file-input');

        // ドロップされたファイルと既存のファイルを合算
        var totalFiles = fileInput.files.length + event.dataTransfer.items.length;

        if (totalFiles > 10) {
            alert('最大で10個のファイルしか選択できません。');
            return;
        }

        for (var i = 0; i < event.dataTransfer.items.length; i++) {
            if (event.dataTransfer.items[i].kind === 'file') {
                var file = event.dataTransfer.items[i].getAsFile();

                // ファイルのバリデーションと画像表示を一緒に行う
                validateAndDisplayImage(file);
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

function validateAndDisplayImage(file) {
    // ここでファイルのバリデーションを実施
    if (file.type.startsWith('image/')) {
        // 画像を表示
        updateInput(file);
        displayImage(file);
    } else {
        alert('選択されたファイルは画像ではありません。');
        // 画像でない場合の処理を追加
    }
}

function displayImage(file) {
    var imageContainer = document.getElementById('image-container');

    var imgWrapper = document.createElement('div');
    imgWrapper.className = 'image-preview';

    var img = document.createElement('img');
    img.src = URL.createObjectURL(file);
    img.alt = 'Image Preview';

    var deleteButton = document.createElement('span');
    deleteButton.className = 'delete-button';
    deleteButton.innerHTML = '×';
    deleteButton.onclick = function () {
        // 削除ボタンがクリックされたらプレビューと input から削除
        imgWrapper.remove();
        removeImageFromInput(file);
    };

    imgWrapper.appendChild(img);
    imgWrapper.appendChild(deleteButton);
    imageContainer.appendChild(imgWrapper);
}

function updateInput(file) {
    var fileInput = document.getElementById('file-input');

    // ファイルリストを取得する前に確認し、存在しない場合は空の配列を代入
    var fileList = fileInput.files || [];

    // FileList は読み取り専用なので、DataTransferオブジェクトを使って更新
    var dataTransfer = new DataTransfer();
    for (var i = 0; i < fileList.length; i++) {
        dataTransfer.items.add(fileList[i]);
    }
    dataTransfer.items.add(file);

    // input 要素に新しい fileList をセット
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
