<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WebGL - Triángulo Animado</title>
    <style>
        canvas {
            display: block;
            margin: auto;
            background-color: #f0f0f0;
        }
    </style>
</head>
<body>
    <canvas id="glCanvas" width="600" height="400"></canvas>
    <script>
        // Obtener el canvas y el contexto WebGL
        const canvas = document.getElementById("glCanvas");
        const gl = canvas.getContext("webgl");

        if (!gl) {
            alert("WebGL no está disponible en tu navegador.");
            throw new Error("WebGL no está disponible.");
        }

        // Definir shaders
        const vertexShaderSource = `
            attribute vec2 aPosition;
            uniform float uTime;
            void main() {
                float x = aPosition.x + sin(uTime) * 0.2;
                gl_Position = vec4(x, aPosition.y, 0.0, 1.0);
            }
        `;

        const fragmentShaderSource = `
            precision mediump float;
            void main() {
                gl_FragColor = vec4(0.0, 0.6, 1.0, 1.0); // Color azul
            }
        `;

        // Función para compilar shaders
        function compileShader(source, type) {
            const shader = gl.createShader(type);
            gl.shaderSource(shader, source);
            gl.compileShader(shader);

            if (!gl.getShaderParameter(shader, gl.COMPILE_STATUS)) {
                console.error(gl.getShaderInfoLog(shader));
                gl.deleteShader(shader);
                return null;
            }

            return shader;
        }

        // Crear y enlazar shaders
        const vertexShader = compileShader(vertexShaderSource, gl.VERTEX_SHADER);
        const fragmentShader = compileShader(fragmentShaderSource, gl.FRAGMENT_SHADER);

        const program = gl.createProgram();
        gl.attachShader(program, vertexShader);
        gl.attachShader(program, fragmentShader);
        gl.linkProgram(program);

        if (!gl.getProgramParameter(program, gl.LINK_STATUS)) {
            console.error(gl.getProgramInfoLog(program));
            gl.deleteProgram(program);
            return;
        }

        gl.useProgram(program);

        // Definir vértices del triángulo
        const vertices = new Float32Array([
            0.0,  0.5,  // Vértice superior
           -0.5, -0.5,  // Vértice inferior izquierdo
            0.5, -0.5   // Vértice inferior derecho
        ]);

        const buffer = gl.createBuffer();
        gl.bindBuffer(gl.ARRAY_BUFFER, buffer);
        gl.bufferData(gl.ARRAY_BUFFER, vertices, gl.STATIC_DRAW);

        const aPosition = gl.getAttribLocation(program, "aPosition");
        gl.vertexAttribPointer(aPosition, 2, gl.FLOAT, false, 0, 0);
        gl.enableVertexAttribArray(aPosition);

        const uTime = gl.getUniformLocation(program, "uTime");

        // Render loop
        function render(time) {
            time *= 0.001; // Convertir a segundos

            gl.clearColor(1.0, 1.0, 1.0, 1.0); // Fondo blanco
            gl.clear(gl.COLOR_BUFFER_BIT);

            gl.uniform1f(uTime, time);

            gl.drawArrays(gl.TRIANGLES, 0, 3);

            requestAnimationFrame(render);
        }

        requestAnimationFrame(render);
    </script>
</body>
</html>
