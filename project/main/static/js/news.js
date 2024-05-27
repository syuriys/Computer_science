function setCardHeights() {
    $('.row').each(function() {
        var tallestTitleHeight = 0;
        var tallestTextHeight = 0;

        $(this).find('.card-title-adjust').each(function() {
            var titleHeight = $(this).height();
            if (titleHeight > tallestTitleHeight) {
                tallestTitleHeight = titleHeight;
            }
        });
        $(this).find('.card-title-adjust').height(tallestTitleHeight);

        $(this).find('.card-text-adjust').each(function() {
            var textHeight = $(this).height();
            if (textHeight > tallestTextHeight) {
                tallestTextHeight = textHeight;
            }
        });
        $(this).find('.card-text-adjust').height(tallestTextHeight);
    });

}


$(document).ready(function() {
    setCardHeights();
  });

  
  






