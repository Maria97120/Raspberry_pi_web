people = function() {
	$(function() {
		
		var myChart = echarts.init(document.getElementById('chart_people'));
		
myChart.setOption({
             title: {
				text: '人流量'
			},
			tooltip: {
				trigger: 'axis'
			},
			legend: {
				x: 'left',
				y: '30px',
				data: ['人数']
			},
			grid: {
				left: '3%',
				right: '4%',
				bottom: '3%',
				containLabel: true
			},
	        toolbox: {
	            show : true,
	            feature : {
	                mark : {show: true},
	                dataView : {show: true, readOnly: false},
	                magicType : {show: true, type: ['line', 'bar']},
	                // restore : {show: true},
	                // saveAsImage : {show: true}
	            }
	        },
	        calculable : true,

             xAxis : [
	            {
	                type : 'category',
	                boundaryGap : false,
	                data : []
	            }
	        ],
             yAxis : [
	            {
	                type : 'value',
	                axisLabel : {
	                    formatter: '{value}'
	                }
	            }
	        ],
             series : [
	            {
	                name:'最多数量',
	                type:'line',
	                data:[],
	                markPoint : {
	                    data : [
	                        {type : 'max', name: '最大值'},
	                        {type : 'min', name: '最小值'}
	                    ]
	                },
	                markLine : {
	                    data : [
	                        {type : 'average', name: '平均值'}
	                    ]
	                }
	            },]
         });
		 
         myChart.showLoading();
		 
         var names=[];  
         var nums=[];  
		 
         $.ajax({
         type : "get",
//       async : true,           
         url : "http://127.0.0.1:5000/people_data",  
//       data : {},
         dataType : "json",      
         success : function(result) {
             
             if (result) {
//           	
                    for(var i=0;i<result["data"].length;i++){
//                  	
                       names.push(result["data"][i]["name"]);  
                     }
                    for(var i=0;i<result["data"].length;i++){
//                  	
                        nums.push(result["data"][i]["pnum"]);    
                      }
                    myChart.hideLoading();    
                    myChart.setOption({       
                        xAxis: {
                            data: names
                        },
                        series: [{
                            name: '人流量',
                            data: nums
                        }]
                    });

             }

        },
         error : function(errorMsg) {
			myChart.hideLoading();
        }
    })
	setTimeout(function() {
			window.onresize = function() {
				rChart.resize();
			}
		}, 200)
	});
}();