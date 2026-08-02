async function loadLibrary() {

    const response = await fetch("library.json");
    const library = await response.json();

    const tree = document.getElementById("library-tree");

    buildTree(library, tree);

}


function buildTree(node, container) {


    Object.keys(node).forEach(key => {

        const item = node[key];


        if (typeof item === "object" && item.file === undefined) {

            const folder = document.createElement("div");
            folder.className = "folder";
            folder.textContent = "▶ " + key;


            const children = document.createElement("div");
            children.style.marginLeft = "15px";
            children.style.display = "none";


            folder.onclick = () => {

                children.style.display =
                    children.style.display === "none"
                    ? "block"
                    : "none";

                folder.textContent =
                    children.style.display === "none"
                    ? "▶ " + key
                    : "▼ " + key;
            };


            container.appendChild(folder);
            container.appendChild(children);


            buildTree(item, children);

        }


        else {

            const file = document.createElement("div");

            file.className = "file";
            file.textContent = key;


            file.onclick = () => {

                loadMarkdown(item.file);

            };


            container.appendChild(file);

        }


    });

}



async function loadMarkdown(path) {


    const response = await fetch(path);

    const markdown = await response.text();


    document.getElementById("content").innerHTML =
        marked.parse(markdown);

}



loadLibrary();
