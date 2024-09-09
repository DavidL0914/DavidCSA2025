---
layout: base
title: David's CSA Page
description: Home Page
hide: true
---
<style>
    body {
    overflow: hidden;
    }
</style>
<body>
    <div id="key" class="draggable"></div>
    <div id="lock" class="lock"></div>
    <div id="message" class="message">I got too lazy to add an easter egg lol</div>

    <script>
        const key = document.getElementById('key');
        const lock = document.getElementById('lock');
        const message = document.getElementById('message');

        // Variables for dragging
        let offsetX, offsetY;
        let isDragging = false;

        key.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.clientX - key.getBoundingClientRect().left;
            offsetY = e.clientY - key.getBoundingClientRect().top;
            document.addEventListener('mousemove', onMouseMove);
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
            document.removeEventListener('mousemove', onMouseMove);
        });

        function onMouseMove(e) {
            if (isDragging) {
                const newX = e.clientX - offsetX;
                const newY = e.clientY - offsetY;
                key.style.left = newX + 'px';
                key.style.top = newY + 'px';
                checkCollision();
            }
        }

        function checkCollision() {
            const keyRect = key.getBoundingClientRect();
            const lockRect = lock.getBoundingClientRect();
            if (isOverlap(keyRect, lockRect)) {
                key.style.display = 'none';
                lock.style.display = 'none';
                showSecret();
            }
        }

        function isOverlap(rect1, rect2) {
            return !(rect2.left > rect1.right ||
                     rect2.right < rect1.left ||
                     rect2.top > rect1.bottom ||
                     rect2.bottom < rect1.top);
        }

        function showSecret() {
            message.style.display = 'block';
            setTimeout(() => {
                message.style.display = 'none';
            }, 5000); 
        }
    </script>
</body>