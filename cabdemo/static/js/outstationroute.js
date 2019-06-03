(function($) {

   'use strict'

    var outstationTaxiRoute;
    var placeFilter = {};
    var tripTypeFilter = {};
    var isSelectedAll = false;
    var init = true;

    var populateRoute = function(){
      fetch('/api/v2/pages/'+route.routeId()+'/').
      then(response => response.json()).
      then(data => {  outstationTaxiRoute = data;
      //console.log(data)
    })
    }

    var routeMap = function(){
      $("#routeMapButton").click(function(e){
        if(init){
          init = false;
          $("#filterPanel").removeClass("hide");
        }else{
          $("#selectAllButton").addClass("hide");
          $("#editButton").removeClass("hide");
          $("#routeMapButton").addClass("hide");
          $("#filterView").addClass("hide");
          showSelectedTagsView();
          generateRoute();
        }
      })
    }

    var showSelectedTagsView = function(){
      $('#selectedFilterView').empty();
      $.each(placeFilter, function(tagKey, tagValue ) {
        $('#selectedFilterView').append("<div class='tag-selected'>"+tagValue+"</div>");
      })
      $.each(tripTypeFilter, function(tripTypeKey, tripTypeValue ) {
        $('#selectedFilterView').append("<div class='tag-selected'>"+tripTypeValue+"</div>");
      })
      $('#selectedFilterView').removeClass('hide');
    }

    var generateRoute = function() {
        if(!$.isEmptyObject(placeFilter) || !$.isEmptyObject(tripTypeFilter)){
            $.each(outstationTaxiRoute.on_route_places.places, function( placeKey, placeValue ) {
              var place = placeValue;
              var locationTags = place.location_tags;
              var tripTypes = place.trip_types;
              var isPlaceFound = false;
              var filterLocationId = "placeOnRoute-"+place.id;
              var filterMapId = "mapBlock-"+place.id;

              $.each(locationTags, function( locationTagKey, locationTagValue ) {
                if(placeFilter[locationTagValue.id] != undefined){
                  $('#'+filterLocationId).removeClass('hide');
                  $('#'+filterMapId).removeClass('hide');
                  isPlaceFound = true;
                  return false;
                }
              });
              if(!isPlaceFound){
                $.each(tripTypes, function( tripTypeKey, tripTypeValue ) {
                  if(tripTypeFilter[tripTypeValue.id] != undefined){
                    $('#'+filterLocationId).removeClass('hide');
                    $('#'+filterMapId).removeClass('hide');
                    isPlaceFound = true;
                    return false;
                  }
                });
              }
              if(!isPlaceFound){
                  $('#'+filterLocationId).addClass('hide');
                  $('#'+filterMapId).addClass('hide');
              }
              isPlaceFound = false;
            });
          } else {
            $('#dynamicRouteMap').children('div').each(function(){
              if($(this).hasClass("hide")){
                $(this).removeClass("hide")
              }
            })
            $('#placesOnRoute').children('div').each(function(){
              if($(this).hasClass("hide")){
                $(this).removeClass("hide")
              }
            })
          }
      }

    var locationTagButtons = function(){
      $('#placeFilter').on('click', function(e){
        e.stopImmediatePropagation()
        if(e.target !== e.currentTarget){
          var tagButton = e.target;
          var tagid = $(tagButton).val();
          var tag = $(tagButton).text();
          if ($(tagButton).hasClass("tag-button-down")) {
              tagButton.classList.add("tag-button-up");
              tagButton.classList.remove("tag-button-down");
              delete placeFilter[tagid];
          } else {
            tagButton.classList.add("tag-button-down");
            tagButton.classList.remove("tag-button-up");
            if(placeFilter[tagid] == undefined)
            {
              placeFilter[tagid]=tag;
            }
          }
        }
      });
    }

    var tripTypeButtons = function(){
      $('#tripTypeFilter').on('click', function(e){
        e.stopImmediatePropagation()
        if(e.target !== e.currentTarget){
          var tripTypeButton = e.target;
          var tripTypeid = $(tripTypeButton).val();
          var tripType = $(tripTypeButton).text();
          if ($(tripTypeButton).hasClass("tripType-button-down")) {
              tripTypeButton.classList.add("tripType-button-up");
              tripTypeButton.classList.remove("tripType-button-down");
              delete tripTypeFilter[tripTypeid];
          } else {
            tripTypeButton.classList.add("tripType-button-down");
            tripTypeButton.classList.remove("tripType-button-up");
            if(tripTypeFilter[tripTypeid] == undefined)
            {
              tripTypeFilter[tripTypeid]=tripType;
            }
          }
        }
      });
    }

    var editFilterButton = function(){
      $('#editButton').on('click', function(e){
        $("#selectAllButton").removeClass("hide");
        $("#editButton").addClass("hide");
        $("#routeMapButton").removeClass("hide");
        $("#filterView").removeClass("hide");
        //enableFilterTags(false);
        $('#selectedFilterView').addClass('hide');
      })
    }

    var selectAllFilterButton = function(){
      $('#selectAllButton').on('click', function(e){
        e.stopImmediatePropagation();
        if(!isSelectedAll){
          $('#placeFilter').children('button').each(function(){
            $(this).addClass("tag-button-down");
            $(this).removeClass("tag-button-up");
            $('#selectAllButton').html("Remove All")
            var tagid = $(this).val();
            var tag = $(this).text();
            if(placeFilter[tagid] == undefined)
            {
              placeFilter[tagid]=tag;
            }
          });
        } else {
          placeFilter={}
          $('#placeFilter').children('button').each(function(){
            $(this).removeClass("tag-button-down");
            $(this).addClass("tag-button-up");
            $('#selectAllButton').html("Select All")
            var tag = $(this).val();
          });
        }
        isSelectedAll=!isSelectedAll;
    });
  }

  $("#like_button_form").submit(function(e){
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'/like/',
        data:{
          route_id:route.routeId(),
          csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
        },
        success:function(data){
          $("#likes_count").html(data.likes_count);
          if(data.is_liked == true){
            $('#like_button').addClass('border-bottom');
          }else{
            $('#like_button').removeClass('border-bottom');
          }
        }
      });
  })

  var reviewButton = function(){
    $("#writeReviewButton").on('click', function(e){
      $("#reviewListPanel").addClass("hide");
      $("#writeReviewPanel").removeClass("hide");
    })
  }


	// Dom Ready
	$(function() {
		populateRoute();
    routeMap();
    locationTagButtons();
    tripTypeButtons();
    editFilterButton();
    selectAllFilterButton();
    reviewButton();
   	});
})(jQuery);
