document.addEventListener("DOMContentLoaded", function() {
    var foldBtns = document.getElementsByClassName("fold-button");
    for (var i = 0; i < foldBtns.length; i++) {
        foldBtns[i].addEventListener("click", function(event) {
            var postDiv = event.target.closest(".one-post");
            if (!postDiv) return;

            if (postDiv.classList.contains("folded")) {
                // Развернуть
                postDiv.classList.remove("folded");
                event.target.innerHTML = "свернуть";
            } else {
                // Свернуть
                postDiv.classList.add("folded");
                event.target.innerHTML = "развернуть";
            }
        });
    }
});