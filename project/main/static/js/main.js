document.addEventListener("DOMContentLoaded", function() {
  var tabLinks = document.querySelectorAll("#v-pills-tab .nav-link");

  tabLinks.forEach(function(link) {
    link.addEventListener("click", function(event) {
      event.preventDefault();
      var activeTab = this.getAttribute("aria-controls");

      var searchParams = new URLSearchParams(window.location.search);
      searchParams.set("active_tab", activeTab.replace("v-pills-", ""));
      searchParams.set("page", 1); 
      window.history.replaceState({}, "", "?" + searchParams.toString());

      tabLinks.forEach(function(tabLink) {
        tabLink.classList.remove("active");
      });

      

      this.classList.add("active");

      var tabContents = document.querySelectorAll(".tab-pane");
      tabContents.forEach(function(content) {
        content.classList.remove("show", "active");
      });
      document.getElementById(activeTab).classList.add("show", "active");
    });
  });

/*   var listItems = document.querySelectorAll('.list-group-item');

  listItems.forEach(function(listItem) {
    var text = listItem.innerHTML;
    var boldText = text.replace(/^(.*?):/, '<strong>$1:</strong>');
    listItem.innerHTML = boldText;
  });
 */
  var courseItems = document.querySelectorAll('.grid-item');
  courseItems.forEach(function(item) {
    var credits = item.getAttribute('data-credits');
    var height = (credits / 30) * 100 + "%";
    item.style.height = height;
  });


  //setCardHeights();
});
/*
  function setCardHeights() {
    $('.row').each(function() {
        var tallestTitleHeight = 0;
        var tallestTextHeight = 0;

        $(this).find('.card-teacher').each(function() {
            var titleHeight = $(this).height();
            if (titleHeight > tallestTitleHeight) {
                tallestTitleHeight = titleHeight;
            }
        });
        $(this).find('.card-teacher').height(tallestTitleHeight);

        $(this).find('.card-position').each(function() {
            var textHeight = $(this).height();
            if (textHeight > tallestTextHeight) {
                tallestTextHeight = textHeight;
            }
        });
        $(this).find('.card-position').height(tallestTextHeight);

        $(this).find('.card-additional').each(function() {
          var textHeight = $(this).height();
          if (textHeight > tallestTextHeight) {
              tallestTextHeight = textHeight;
          }
      });
      $(this).find('.card-additional').height(tallestTextHeight);
    });

}

$(document).ready(function() {
  setCardHeights();
});
*/




