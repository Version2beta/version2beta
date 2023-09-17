/*
 * multiup.js - jQuery Plugin for selecting multiple files for uploading 
 * written by Rob Martin, rob@qmuxs.com
 * (c) 2011 Quintessential Mischief LLC
 *
 * Version 0.1.0 - initial release
 * Dual licensed under the MIT and GPL licenses
 * http://www.opensource.org/licenses/mit-license.php
 * http://www.gnu.org/licenses/gpl.html
 *
 * Just for clarification, this does not do anything ajaxy. 
 * Requires jQuery. Tested with version 1.6.2 but should work with older.
 * Technique inspired by Stickman http://www.the-stickman.com 

 * Options:
 * deleteButton: Element to use for removing items from file cabinet. Default is '<span>X</span>'.
 * inputName: Name of input type file. Defaults to 'file[]';
 * listingCSSAfter: CSS appended to the listing in the file cabinet. Default is '</p>'.
 * listingCSSBefore: CSS prepended to the listing in the file cabinet. Default is '<p>'.
 * max: Maximum number of files to select. 0 is no limit. Default is 0.
 */
;(function($) {
var ver = '0.1.0';

$.fn.multiup = function(options) {
  // Initialize
  var opts = $.extend({}, $.fn.multiup.defaults, options || {});
  var $cabinet = $(this);
  var count = 0;
  var fileCurrent;
  $(this).addClass('multiup-cabinet');

  addF = function() {
    fileCurrent = $('<input type="file" name="'+opts.inputName+'" />');
    fileCurrent.addClass('multiup-input');
    fileCurrent.change(function() {
      $(this).css({
        'position': 'absolute',
        'left': -10000
      })
      listF(this);
      addF();
    });
    moreF(1);
    fileCurrent.insertBefore($cabinet);
  };

  listF = function(file) {
    // Add the selected file to the list in the file cabinet
    var itemParent = $(file).get();
    var itemCurrent = $(opts.listingCSSBefore+$(itemParent).val()+opts.listingCSSAfter);
    var deleteButton = $(opts.deleteButton);
    itemCurrent.addClass('multiup-listing');
    if (count % 2) { itemCurrent.addClass('multiup-odd'); }
    deleteButton.addClass('multiup-delete');
    deleteButton.click(function() {
      $(itemParent).remove();
      $(this).parent('p').remove();
      moreF(-1);
      return false;
    });
    deleteButton.prependTo(itemCurrent);
    itemCurrent.appendTo($cabinet);
  };

  moreF = function(n) { 
    count = count + n;
    if (opts.max && count>opts.max) {
      fileCurrent.attr('disabled', 'disabled');
    } else {
      fileCurrent.removeAttr('disabled');
    }
  }

  addF();
};

$.fn.multiup.ver = function() { return ver; };
$.fn.multiup.defaults = {
  inputName: 'file[]', 
  max: 0, 
  deleteButton: '<span>X</span>',
  listingCSSBefore: '<p>',
  listingCSSAfter: '</p>'
};

})(jQuery);
