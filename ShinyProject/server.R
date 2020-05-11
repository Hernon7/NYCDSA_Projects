shinyServer(function(input, output,session) {
  
  
  
  
  
# plots in the data tab
  output$table <- DT::renderDataTable({
    datatable(steamdata, rownames=FALSE) %>%
      formatStyle(input$selected,
                  background="skyblue", fontWeight='bold')
    # Highlight selected column using formatStyle
  })
  
  


 # plots in the wordcloud tab
  output$wordcloud = renderPlot(

    wordcloud(wordcloud$developer, wordcloud$number,scale=c(4,0.08),
                  min.freq = input$freq, max.words=input$max,
                  colors=brewer.pal(8, "Dark2"))

  )


  
# plots in the time tab
  
  output$time = renderGvis( gvisAnnotationChart(linetable, datevar="Release_date",
                            numvar="Game_number",
                            options=list(displayAnnotations=TRUE,
                                         legendPosition='newRow',
                                         width=1000, height=600) 
                            )
  )
  

# plots in the playtime tab

  output$playtime1 = renderGvis(


    gvisBarChart(avgtime,options=list(displayAnnotations=TRUE,
                                        legendPosition='newRow',
                                        width=1000, height=600) )

      )

  output$playtime2 = renderGvis(


    gvisBarChart(medtime,options=list(displayAnnotations=TRUE,
                                      legendPosition='newRow',
                                      width=1000, height=600) )

  )


# plots in the platform tab
  output$platforms = renderGvis(
    
    gvisColumnChart(platformdf %>% select(.,input$genres) ,options = list(width = 600,height = 600))
  )

  output$review = renderGvis(
    # gvisColumnChart(bardata %>% filter(.,genres == input$genres) ,options = list(width = 600,height = 600)),
    gvisPieChart( data.frame(
      review = colnames(bardata %>% filter(.,genres ==input$genres) %>% select(-1)),
      value = as.numeric (as.vector(bardata %>% filter(.,genres == input$genres) %>% select(-1)))
    ),options = list(width = 600,height = 600))
  )
  
  
# plots in the  tab owners
  
  output$price_owners = renderGvis(
    gvisBarChart(price_owners,options=list(displayAnnotations=TRUE,
                                   legendPosition='newRow',
                                   width=1000, height=600) )
  )
  
  
  output$time_owners = renderGvis(
    gvisBarChart(time_owners,options=list(displayAnnotations=TRUE,
                                           legendPosition='newRow',
                                           width=1000, height=600) )
  )
  
  

})



