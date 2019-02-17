rain = function() {
	$(function() {
		
		var rChart = echarts.init(document.getElementById('chart_rain'));
		
		rChart.setOption({
             title: {
				text: '降雨量（单位：mm）'
			},
			color: ['#3398DB'],
			tooltip: {
				trigger: 'axis',
				axisPointer : {            
            		type : 'shadow'       
        		}
			},
			legend: {
				x: 'left',
				y: '30px',
				data: ['雨量']
			},
			grid: {
				left: '3%',
				right: '0%',
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
	                data : [],
					axisTick: {
                		alignWithLabel: true
            		}
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
	                type:'bar',
	                data:[],
					barWidth: '60%',
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
		 
         rChart.showLoading();
		 
         var names=[];  
         var nums=[];  
		 
         $.ajax({
         type : "get",
//       async : true,           
         url : "http://127.0.0.1:5000/rain_data",  
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
                        nums.push(result["data"][i]["rnum"]);    
                      }
                    rChart.hideLoading();    
                    rChart.setOption({       
                        xAxis: {
                            data: names
                        },
                        series: [{
                            name: '降雨量',
                            data: nums
                        }]
                    });

             }

        },
         error : function(errorMsg) {
			rChart.hideLoading();
        }
    })
	setTimeout(function() {
			window.onresize = function() {
				rChart.resize();
			}
		}, 200)
	});
}();