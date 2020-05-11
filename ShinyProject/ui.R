




shinyUI(dashboardPage(
  skin = "black",
 
  dashboardHeader(title = "ShinyProject"),

  
  dashboardSidebar(
    sidebarUserPanel("STEAM", image = 'steam.png'),
    sidebarMenu(
      menuItem(
        "Introduction",
        tabName = "intro",
        icon = icon("desktop")
      ),
      
      menuItem("Data", tabName = "data", icon = icon("database")),
      
      menuItem("Time", tabName = "time", icon = icon("line-chart")),
      
      menuItem("Platforms", tabName = "platforms", icon = icon("gamepad")),
      
      menuItem("Playtime", tabName = "playtime", icon = icon("clock-o")),
      
      menuItem("Owners", tabName = "owners", icon = icon("trophy"))
      
      
    )
  ),
  dashboardBody(
    tabItems(
      tabItem(
        tabName = "intro",
        column(width = 12,box(width = NULL,
        h3("Steam is a video game digital distribution platform developed by Valve Corporation.It was launched in September 2003 as a way for Valve to provide automatic updates to their games, but eventually expanded to include non-Valve games from third-party publishers."),
        h3("Steam offers digital rights management (DRM), matchmaking servers, video streaming, and social networking services.
 It also provides the user with installation and automatic updating of games, and community features such as friends lists and groups, cloud saving, and in-game voice and chat functionality."),
        collapsible = TRUE,
        title = "STEAM Introduction",
        status = "primary",
        solidHeader = TRUE)),
        
        
        fluidRow(box(width = 8,
      column( width = 3,sliderInput(
        "freq",
        "Minimum Frequency:",
        min = 1,
        max = 50,
        value = 25
      ),
      sliderInput(
        "max",
        "Maximum Number of Words:",
        min = 1,
        max = 15,
        value = 15)),   
		  column( width = 5,
          plotOutput("wordcloud")),collapsible = TRUE,
          title = "Developer wordcloud",
          status = "primary",
          solidHeader = TRUE)
		                        
		  )
      ),
      
      
      
      
      tabItem(tabName = "time",
              
              fluidRow(column(
                width = 10,
                box(
                  width = NULL,
                  htmlOutput("time"),
                  collapsible = TRUE,
                  title = "Historical Plot",
                  status = "primary",
                  solidHeader = TRUE
                )
                
              ))),
      
      
      
      
      tabItem(tabName = "playtime",
              fluidRow (column(
                width = 10, tabBox(width = NULL,
                                   tabPanel(
                                     h5("Average Play Time"),
                                     htmlOutput("playtime1")
                                   ),
                                   tabPanel(
                                     h5("Median Play Time"),
                                     htmlOutput("playtime2")
                                   ))
              ))),
      
      
      tabItem(
        tabName = "platforms",
        selectInput("genres", "Genres:",
                    choices = colnames(platformdf)[-1]),
        helpText("Data based on different genres."),
        hr(),
        
        fluidRow(
          box(
            width = NULL,
            column(width = 4, htmlOutput("platforms")),
            column(width = 6, htmlOutput("review")),
            collapsible = TRUE,
            title = "Plot",
            status = "primary",
            solidHeader = TRUE
            
          )
          
        )
        
      ),
      
      
      tabItem(
        tabName = "data",
        selectizeInput("selected",
                       "Select Item to Display",
                       choice = colnames(steam_raw)[-1]),
        fluidRow(
          box(
            DT::dataTableOutput("table"),
            width = 30,
            collapsible = TRUE,
            title = "Data",
            status = "primary",
            solidHeader = TRUE
          )
        )
      ),
      
      
      tabItem(tabName = "owners",
              fluidRow(column(
                width = 10, tabBox(width = NULL,
                                   tabPanel(
                                     h5("Price"),
                                     htmlOutput("price_owners")
                                   ),
                                   tabPanel(
                                     h5("Play Time"),
                                     htmlOutput("time_owners")
                                   ))
              )))
      
    )
  )
  
))

