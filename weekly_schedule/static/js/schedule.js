$(document).ready(function(){
    $(".checkbox").change(function(){
        var data = $(this);
        if ($(this).attr('cek') == 'false'){
            $(".schedule-name").addClass('strike-through');
            $(this).attr('cek','true');
            console.log('line-through');
        } else{
            $(".schedule-name").removeClass('strike-through')
            console.log('not line-through');
            $(this).attr('cek','false');
        }
    });

    $(".complete-btn").click(function() {
        console.log("Delete Task...");

		var listItem=this.parentNode;
		var ul=listItem.parentNode;
		//Remove the parent list item from the ul.
		ul.removeChild(listItem);
        
    });
});