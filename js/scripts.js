$(function(){
  var documentEl = $(window), fadeElem = $('.content');


  documentEl.on('scroll', function() {
      var currScrollPos = documentEl.scrollTop();

      fadeElem.each(function() {
          var $this = $(this), elemOffsetTop = $this.offset().top;

          if (currScrollPos > elemOffsetTop)
            $this.css('opacity', 1 - (currScrollPos-elemOffsetTop)/400);

          if (currScrollPos === elemOffsetTop)
            $this.css('opacity', 1);

          if (currScrollPos < elemOffsetTop)
            $this.css('opacity', 1 - (elemOffsetTop - currScrollPos)/800);
      });

  });

});
