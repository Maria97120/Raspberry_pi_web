rasp1 = function() {
	$(function() {

		var r3Chart = echarts.init(document.getElementById('r3'));

		var colors = ['#5793f3', '#d14a61', '#675bba'];

		r3Chart.setOption({
			
			color: colors,
			
			tooltip: {
				trigger: 'axis',
				axisPointer: {
					type: 'cross'
				}
			},
			grid: {
				right: '20%'
			},
			toolbox: {
				feature: {
					dataView: {
						show: true,
						readOnly: false
					},
					restore: {
						show: true
					},
					saveAsImage: {
						show: true
					}
				}
			},
			legend: {
				data: ['降水量', '湿度', '温度']
			},
			xAxis: [{
				type: 'category',
				axisTick: {
					alignWithLabel: true
				},
				data: []
			}],
			yAxis: [{
				type: 'value',
				name: '降水量',
				position: 'right',
				axisLine: {
					lineStyle: {
						color: colors[0]
					}
				},
				axisLabel: {
					formatter: '{value} ml'
				}
			}, {
				type: 'value',
				name: '湿度',
				position: 'right',
				offset: 80,
				axisLine: {
					lineStyle: {
						color: colors[1]
					}
				},
				axisLabel: {
					formatter: '{value} %'
				}
			}, {
				type: 'value',
				name: '温度',
				position: 'left',
				axisLine: {
					lineStyle: {
						color: colors[2]
					}
				},
				axisLabel: {
					formatter: '{value} °C'
				}
			}],
			series: [{
				name: '降水量',
				type: 'bar',
				data: []
			}, {
				name: '温度',
				type: 'line',
				yAxisIndex: 1,
				data: []
			}, {
				name: '湿度',
				type: 'line',
				yAxisIndex: 2,
				data: []
			}]
		
         });
		 
         r3Chart.showLoading();
		 
        var names=[];  
        var rnums=[]; 
		var tnums=[];
		var hnums=[];
			
		 
         $.ajax({
         type : "get",
//       async : true,           
         url : "http://127.0.0.1:5000/rasp3_data",  
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
                        rnums.push(result["data"][i]["rnum"]);    
                      }
					for(var i=0;i<result["data"].length;i++){
//                  	
                        hnums.push(result["data"][i]["hnum"]);    
                      }
					for(var i=0;i<result["data"].length;i++){
//                  	
                        tnums.push(result["data"][i]["tnum"]);    
                      }
                    r3Chart.hideLoading();    
                    r3Chart.setOption({       
                        xAxis: {
                            data: names
                        },
                        series: [{
                            name: '降水量',
                            data: rnums
                        },{
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
			r3Chart.hideLoading();
        }
    })
			
		
		var p3Chart = echarts.init(document.getElementById('people3'));

		p3Chart.setOption({
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
		 
         p3Chart.showLoading();
		 
         var pnums=[];
		 var rnames=[];
		 
         $.ajax({
         type : "get",
//       async : true,           
         url : "http://127.0.0.1:5000/rasp3_data",  
//       data : {},
         dataType : "json",      
         success : function(result) {
             
             if (result) {
					for(var i=0;i<result["data"].length;i++){
//                  	
                        rnames.push(result["data"][i]["name"]);    
                      }
                    for(var i=0;i<result["data"].length;i++){
//                  	
                        pnums.push(result["data"][i]["pnum"]);    
                      }
                    p3Chart.hideLoading();    
                    p3Chart.setOption({       
                        xAxis: {
                            data: rnames
                        },
                        series: [{
                            name: '人流量',
                            data: pnums
                        }]
                    });

             }

        },
         error : function(errorMsg) {
			p3Chart.hideLoading();
        }
    })
		
		setTimeout(function() {
			window.onresize = function() {
				r3Chart.resize();
				p3Chart.resize();
			}
		}, 200)
	});
}();