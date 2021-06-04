/*
 * generate by tool
*/
//using System.Collections;
//using System.Collections.Generic;
//using System.Linq;
//using LitJson;
//using FixedPointy;
namespace Table
{
    
    
    
       
    public class HeroInfo : BaseTable
    {
        
        /// <summary>
        ///ID
        /// </summary>
        public int id; 
        
        /// <summary>
        ///英雄名称
        /// </summary>
        public string name; 
        
        /// <summary>
        ///英雄介绍
        /// </summary>
        public string describe; 
        
        /// <summary>
        ///战斗模型Id(先填资源id 之后换成另一张表格过度)
        /// </summary>
        public int modelId; 
        

        
        public int Id { get => id; }     
        
        public string Name { get => name; }     
        
        public string Describe { get => describe; }     
        
        public int Modelid { get => modelId; }     
        

    } 
}