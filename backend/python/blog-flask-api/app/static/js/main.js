document.addEventListener("DOMContentLoaded", () => {
    const posts = document.querySelectorAll(".post");

    posts.forEach((post, index) => {
        post.style.opacity = 0;
        setTimeout(() => {
            post.style.transition = "0.5s";
            post.style.opacity = 1;
        }, index * 150);
    });
});