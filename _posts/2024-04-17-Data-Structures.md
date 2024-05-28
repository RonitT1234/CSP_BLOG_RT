<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Tree Builder</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .tree-container {
            position: relative;
            width: 100%;
            height: 600px;
            border: 1px solid #ccc;
            overflow: auto;
        }
        .tree-node {
            position: absolute;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            border-radius: 50%;
            background-color: #4CAF50;
            color: white;
            text-align: center;
        }
        .tree-node input {
            width: 35px;
            height: 20px;
            border: none;
            text-align: center;
            font-size: 14px;
        }
        svg {
            position: absolute;
            width: 100%;
            height: 100%;
        }
        #tree-controls {
            margin-bottom: 20px;
        }
        #tree-controls button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            margin: 5px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        #tree-controls button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <h1>Number Tree Builder</h1>
    <div id="tree-controls">
        <button onclick="addNode()">Add Root Node</button>
        <button onclick="inOrderTraversal()">In-order Traversal</button>
        <button onclick="preOrderTraversal()">Pre-order Traversal</button>
        <button onclick="postOrderTraversal()">Post-order Traversal</button>
        <button onclick="levelOrderTraversal()">Level-order Traversal</button>
        <button onclick="findGreatestNumber()">Find Greatest Number</button>
    </div>
    <div class="tree-container" id="tree-container"></div>
    <div id="result"></div>
    <script>
        class TreeNode {
            constructor(value) {
                this.value = value;
                this.left = null;
                this.right = null;
                this.x = 0;
                this.y = 0;
            }
        }
        let root = null;

        function createNodeElement(node) {
            const nodeElement = document.createElement('div');
            nodeElement.className = 'tree-node';
            nodeElement.innerHTML = `
                <input type="number" value="${node.value !== null ? node.value : ''}" onblur="updateNodeValue(this)">
                <button onclick="addChildNode(this, 'left')">L</button>
                <button onclick="addChildNode(this, 'right')">R</button>
            `;
            node.element = nodeElement;
            return nodeElement;
        }

        function addNode() {
            if (root === null) {
                root = new TreeNode(null);
                document.getElementById('tree-container').appendChild(createNodeElement(root));
                renderTree();
            }
        }

        function updateNodeValue(input) {
            const value = input.value;
            const node = findNodeByElement(input.parentElement);
            node.value = parseInt(value, 10);
            renderTree();
        }

        function addChildNode(button, position) {
            const parentNode = findNodeByElement(button.parentElement);
            if (!parentNode[position]) {
                parentNode[position] = new TreeNode(null);
                document.getElementById('tree-container').appendChild(createNodeElement(parentNode[position]));
                renderTree();
            }
        }

        function findNodeByElement(element, currentNode = root) {
            if (!currentNode) return null;
            if (currentNode.element === element) return currentNode;
            return findNodeByElement(element, currentNode.left) || findNodeByElement(element, currentNode.right);
        }

        function renderTree() {
            const container = document.getElementById('tree-container');
            container.innerHTML = '';
            const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
            container.appendChild(svg);
            if (root) {
                positionNodes(root, 0, container.clientWidth, 20);
                drawTree(root, container, svg);
            }
        }

        function positionNodes(node, xMin, xMax, y) {
            if (node === null) return;
            const xMid = (xMin + xMax) / 2;
            node.x = xMid;
            node.y = y;
            positionNodes(node.left, xMin, xMid, y + 80);
            positionNodes(node.right, xMid, xMax, y + 80);
        }

        function drawTree(node, container, svg) {
            if (node === null) return;
            if (node.left) drawLine(node, node.left, svg);
            if (node.right) drawLine(node, node.right, svg);
            drawNode(node, container);
            drawTree(node.left, container, svg);
            drawTree(node.right, container, svg);
        }

        function drawNode(node, container) {
            const nodeDiv = createNodeElement(node);
            nodeDiv.style.left = `${node.x - 20}px`;
            nodeDiv.style.top = `${node.y - 20}px`;
            container.appendChild(nodeDiv);
        }

        function drawLine(parent, child, svg) {
            const line = document.createElementNS('http://www.w3.org/2000/svg', 'line');
            line.setAttribute('x1', parent.x);
            line.setAttribute('y1', parent.y + 20);
            line.setAttribute('x2', child.x);
            line.setAttribute('y2', child.y - 20);
            line.setAttribute('stroke', 'black');
            line.setAttribute('stroke-width', '2');
            svg.appendChild(line);
        }

        function inOrderTraversal() {
            const result = [];
            function traverse(node) {
                if (node !== null) {
                    traverse(node.left);
                    if (node.value !== null) result.push(node.value);
                    traverse(node.right);
                }
            }
            traverse(root);
            document.getElementById('result').innerText = 'In-order Traversal: ' + result.join(', ');
        }

        function preOrderTraversal() {
            const result = [];
            function traverse(node) {
                if (node !== null) {
                    if (node.value !== null) result.push(node.value);
                    traverse(node.left);
                    traverse(node.right);
                }
            }
            traverse(root);
            document.getElementById('result').innerText = 'Pre-order Traversal: ' + result.join(', ');
        }

        function postOrderTraversal() {
            const result = [];
            function traverse(node) {
                if (node !== null) {
                    traverse(node.left);
                    traverse(node.right);
                    if (node.value !== null) result.push(node.value);
                }
            }
            traverse(root);
            document.getElementById('result').innerText = 'Post-order Traversal: ' + result.join(', ');
        }

        function levelOrderTraversal() {
            const result = [];
            const queue = [];
            if (root !== null) {
                queue.push(root);
                while (queue.length > 0) {
                    const node = queue.shift();
                    if (node.value !== null) result.push(node.value);
                    if (node.left !== null) queue.push(node.left);
                    if (node.right !== null) queue.push(node.right);
                }
            }
            document.getElementById('result').innerText = 'Level-order Traversal: ' + result.join(', ');
        }

        function findGreatestNumber() {
            function findMax(node) {
                if (node === null) return -Infinity;
                const leftMax = findMax(node.left);
                const rightMax = findMax(node.right);
                return Math.max(node.value, leftMax, rightMax);
            }
            const greatestNumber = findMax(root);
            document.getElementById('result').innerText = 'Greatest Number: ' + (greatestNumber === -Infinity ? 'Tree is empty' : greatestNumber);
        }
    </script>
</body>
</html>
