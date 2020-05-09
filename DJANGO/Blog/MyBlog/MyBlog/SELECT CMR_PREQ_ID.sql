SELECT CMR_PREQ_ID ,
    PROJECT_NUMBER,
    PROJECT_NAME,
    DESCRIPTION,
    START_DATE,
    END_DATE,
    STATUS,
    test,
    DATE_GENERATION,
    sum(Amount)||' €' "Amount",
   LISTAGG(volume, CHR(13)) WITHIN GROUP (ORDER BY volume DESC)  vol
    --total_hours,
    --VOLUME,
    --DATE_GENERATION,
    --CREATED_DATE,
    --ACCEPT_REJECT_DATE,
   -- SUM(Amount)||'€',
   -- SUM(total_hours)

    
    
    FROM (
select 
    a.CMR_PREQ_ID as CMR_PREQ_ID,
    a.PROJECT_NUMBER,
    a.PROJECT_NAME,
    a.DESCRIPTION,
    a.START_DATE,
    a.END_DATE,
   case
       when a.STATUS = 'Purchase Request Accepted by ECM Sales Backoffice' then 'PR Accepted' 
       when a.STATUS = 'Purchase Request Rejected by ECM Sales Backoffice' then 'PR Rejected'
       when a.STATUS = 'Invoice Created by ECM Finance & Accounting' then 'Invoice Created'
       when a.STATUS = 'Invoice Confirmed by CMORE Finance' then 'Invoice Confirmed'
       when a.STATUS = 'PR created by CMORE PM' then 'PR Created'
       when a.STATUS = 'Quotation Rejected by CMORE Project Manager' then 'Quotation Rejected'
       when a.STATUS = 'Quotation Accepted by CMORE Project Manager' then 'Quotation Accepted'
       when a.STATUS = 'Quotation created by ECM Sales Backoffice' then 'Quotation Created'
       when a.STATUS = 'DN Uploaded by ECM Finance & Accounting' then 'DN Uploaded'
       when a.STATUS = 'DN Created by ECM Finance & Accounting' then 'DN Created'
       when a.STATUS = 'DN Confirmed by CMORE Project Manager' then 'DN Confirmed'
       when a.STATUS = 'PO Created by CMORE Purchase Department' then 'PO Created'
       when a.STATUS = 'PO Confirmed by ECM Finance & Accounting' then 'PO Confirmed'
       when a.STATUS = 'PO Uploaded by CMORE Purchase Department' then 'PO Uploaded'
       when a.STATUS = 'Invoice Uploaded by ECM Finance & Accounting' then 'Invoice Uploaded'
    else a.STATUS
    end Status,
    a.DATE_GENERATION,
    a.CREATED_DATE,
  
    (select RESPONSIBLE_PERSON_NAME from CMR_PR_RESPRSN where CMR_PR_RESPRSN_ID=(select CMR_PR_RESPRSN_ID from CMR_PREQ_2_RESPRSN where CMR_PREQ_ID= a.CMR_PREQ_ID)) as CMOREProjectManager,
    case
    when a.STATUS = 'Purchase Request Accepted by ECM Sales Backoffice' then 'PurchaseRequestAccepted' 
    when a.STATUS = 'Purchase Request Rejected by ECM Sales Backoffice' then 'PurchaseRequestRejected'
    when a.STATUS = 'PR created by CMORE PM' then 'PRCreated'
    end test,
      --(select (sum(AMOUNT)|| ' €') from CMR_PREQ_2_SERVICETYPE where a.CMR_PREQ_ID =  a.CMR_PREQ_ID ) Amount,
      a.ACCEPT_REJECT_DATE,
  case 
       when b.MAN_UNIT = 'Hours'    and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Hour'
       when b.MAN_UNIT = 'Frame'    and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Frame'
       when b.MAN_UNIT = 'Image'    and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Image'
       when b.MAN_UNIT = 'Session'  and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Session'
       when b.MAN_UNIT = 'Traces'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Trace'
       when b.MAN_UNIT = 'Object'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Object'
       when b.MAN_UNIT = 'Box'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN   ||' '||'Box'


       when b.MAN_UNIT = 'Hours'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Hours'
       when b.MAN_UNIT = 'Frame'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Frames'
       when b.MAN_UNIT = 'Image'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Images'
       when b.MAN_UNIT = 'Session' and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Sessions'
       when b.MAN_UNIT = 'Traces'  and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Traces'
       when b.MAN_UNIT = 'Object'  and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Objects'
       when b.MAN_UNIT = 'Box'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN   ||' '||'Boxes'
       
       when b.MAN_UNIT = '1'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Days'
       when b.MAN_UNIT = '0'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Hours'
       when b.MAN_UNIT = '3'  and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Months'
       when b.MAN_UNIT = '2' and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Weeks'
      
       when b.MAN_UNIT = '1'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Day'
       when b.MAN_UNIT = '0'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Hours'
       when b.MAN_UNIT = '3'  and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Month'
       when b.MAN_UNIT = '2' and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Week'
 
 
      -- New one 
       when b.MAN_UNIT = 'Man Day'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Days'
       when b.MAN_UNIT = 'Man Hours'   and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Hours'
       when b.MAN_UNIT = 'Man Month' and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Months'
       when b.MAN_UNIT = 'Man Week' and b.TOTAL_VOLUMN <> 1   then b.TOTAL_VOLUMN  ||' '||'Weeks'
       
        when b.MAN_UNIT = 'Man Day'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Day'
        when b.MAN_UNIT = 'Man Hours'  and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Hours'
        when b.MAN_UNIT = 'Man Month'   and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Month'
        when b.MAN_UNIT = 'Man Week'  and b.TOTAL_VOLUMN = 1   then b.TOTAL_VOLUMN  ||' '||'Week'
  else 
  null
  end Volume , 
  --from CMR_PREQ_2_SERVICETYPE a, CMR_PREQ b  
     -- b.TOTAL_VOLUMN ||' '|| b.MAN_UNIT,
  b.AMOUNT as Amount,
  b.total_hours,
    B.CMR_PREQ_2_SERVICETYPE_ID
from 
    CMR_PREQ a inner join CMR_PREQ_2_SERVICETYPE b on a. CMR_PREQ_ID = b.CMR_PREQ_ID     
where 
 --   EXTRACT (MONTH FROM a.START_DATE) >=  :P35_START_DATE
        EXTRACT (MONTH FROM a.END_DATE) >=  :P35_START_DATE
and 
    EXTRACT (MONTH FROM a.END_DATE) <=  :P35_END_DATE )
    
group BY CMR_PREQ_ID ,
    PROJECT_NUMBER,
    PROJECT_NAME,
    DESCRIPTION,
    START_DATE,
    END_DATE,
    STATUS,
    test,
    DATE_GENERATION
    --Amount,
    --total_hours
    
   -- VOLUME,
   -- DATE_GENERATION,
   -- CREATED_DATE,
   -- ACCEPT_REJECT_DATE
    
--and (status='Purchase Request Accepted by ECM Sales Backoffice' or status='Purchase Request Rejected by ECM Sales Backoffice' or status='PR created by CMORE PM');

