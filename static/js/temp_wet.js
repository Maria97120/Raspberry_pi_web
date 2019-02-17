temp_wet = function() {
	$(function() {
		
		var tChart = echarts.init(document.getElementById('chart_temp'));
		
		tChart.setOption({
             title: {
				text: '温度/湿度'
			},
			tooltip: {
				trigger: 'axis'
			},
			legend: {
				x: 'left',
				y: '30px',
				data: ['湿度', '温度']
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
	                type : 'value'	            
	            }
	        ],
             series : [
	            {
	                name:'湿度',
	                type:'line',
					stack: '%',
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
	            },{
					name:'温度',
	                type:'line',
					stack: 'C%',
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
					
				}]
         });
		 
         tChart.showLoading();
		 
        var names=[];  
        var tnums=[]; 
		var hnums=[];
		
		 
         $.ajax({
         type : "get",
//       async : true,           
         url : "http://127.0.0.1:5000/tem_hum_data",  
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
                        tnums.push(result["data"][i]["tnum"]);    
                      }
					for(var i=0;i<result["data"].length;i++){
//                  	
                        hnums.push(result["data"][i]["hnum"]);    
                      }
                    tChart.hideLoading();    
                    tChart.setOption({       
                        xAxis: {
                            data: names
                        },
                        series: [{
                            name: '温度',
                            data: tnums
                        },{
							name: '湿度',
                            data: hnums
						}]
                    });

             }

        },
         error : function(errorMsg) {
			tChart.hideLoading();
        }
    })
	setTimeout(function() {
			window.onresize = function() {
				rChart.resize();
			}
		}, 200)
		
	});
}();